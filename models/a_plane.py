from models.transport import Transport_device


class A_plane(Transport_device):
    def __init__(self, meal, starting_address, final_address, clases):
        super().__init__(meal, starting_address, final_address, clases)

    def __str__(self) -> str:
        return f"{self.meal}-{self.starting_address}-{self.final_address}-{self.clases}"


class A_planes:
    def __init__(self, path_to_file) -> None:
        self.list_of_planes = []
        self.path_to_file = path_to_file

    def add_plane(self, plane: Transport_device):
        self.list_of_planes.append(plane)

    def list_planes(self):
        for plane in self.list_of_planes:
            print(plane)

    def initialise_plane(self):
        p = open(self.path_to_file, "r")
        for plane in p:
            plane = A_plane(
                plane.split()[0],
                plane.split()[1],
                plane.split()[2],
                plane.split()[3],
            )
            self.add_plane(plane)
    
    def find_planes(self, meal_t, starting_address_t, final_address_t) -> A_plane:
        for plane in self.list_of_planes:
            if (
                plane.meal == meal_t
                and plane.starting_address == starting_address_t
                and plane.final_address == final_address_t
            ):
                return A_plane(
                    plane.meal, plane.starting_address, plane.final_address, plane.clases
                )

