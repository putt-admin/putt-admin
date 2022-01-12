<template>
  <div class="row">
    <div class="col-6">
      <div class="card">
        <div class="card-header">
          <h4>App Menu</h4>
          <div class="card-header-action"></div>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-striped" id="sortable-table">
              <thead>
                <tr>
                  <th class="text-center">
                    <i class="fas fa-th"></i>
                  </th>
                  <th>Menu</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <div class="sort-handler">
                      <i class="fas fa-th"></i>
                    </div>
                  </td>
                  <td>Create a mobile app</td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
                <tr>
                  <td>
                    <div class="sort-handler">
                      <i class="fas fa-th"></i>
                    </div>
                  </td>
                  <td>Redesign homepage</td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="col-6">
      <div class="card">
        <div class="card-header">
          <h4>All Pages</h4>
          <div class="card-header-action">
            <div class="input-group-btn">
              <button class="btn btn-primary">
                <i class="fas fa-search"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-striped" id="sortable-table">
              <thead>
                <tr>
                  <th>Task Name</th>
                  <th>Progress</th>
                  <th>Members</th>
                  <th>Due Date</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Create a mobile app</td>
                  <td class="align-middle">
                    <div
                      class="progress"
                      data-height="4"
                      data-toggle="tooltip"
                      title="100%"
                    >
                      <div
                        class="progress-bar bg-success"
                        data-width="100"
                      ></div>
                    </div>
                  </td>
                  <td>
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-5.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Wildan Ahdian"
                    />
                  </td>
                  <td>2018-01-20</td>
                  <td><div class="badge badge-success">Completed</div></td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
                <tr>
                  <td>Redesign homepage</td>
                  <td class="align-middle">
                    <div
                      class="progress"
                      data-height="4"
                      data-toggle="tooltip"
                      title="0%"
                    >
                      <div class="progress-bar" data-width="0"></div>
                    </div>
                  </td>
                  <td>
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-1.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Nur Alpiana"
                    />
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-3.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Hariono Yusup"
                    />
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-4.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Bagus Dwi Cahya"
                    />
                  </td>
                  <td>2018-04-10</td>
                  <td><div class="badge badge-info">Todo</div></td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
                <tr>
                  <td>Backup database</td>
                  <td class="align-middle">
                    <div
                      class="progress"
                      data-height="4"
                      data-toggle="tooltip"
                      title="70%"
                    >
                      <div
                        class="progress-bar bg-warning"
                        data-width="70"
                      ></div>
                    </div>
                  </td>
                  <td>
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-1.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Rizal Fakhri"
                    />
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-2.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Hasan Basri"
                    />
                  </td>
                  <td>2018-01-29</td>
                  <td><div class="badge badge-warning">In Progress</div></td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
                <tr>
                  <td>Input data</td>
                  <td class="align-middle">
                    <div
                      class="progress"
                      data-height="4"
                      data-toggle="tooltip"
                      title="100%"
                    >
                      <div
                        class="progress-bar bg-success"
                        data-width="100"
                      ></div>
                    </div>
                  </td>
                  <td>
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-2.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Rizal Fakhri"
                    />
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-5.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Isnap Kiswandi"
                    />
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-4.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Yudi Nawawi"
                    />
                    <img
                      alt="image"
                      src="assets/img/avatar/avatar-1.png"
                      class="rounded-circle"
                      width="35"
                      data-toggle="tooltip"
                      title="Khaerul Anwar"
                    />
                  </td>
                  <td>2018-01-16</td>
                  <td><div class="badge badge-success">Completed</div></td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
