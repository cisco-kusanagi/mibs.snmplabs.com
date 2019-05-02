#
# PySNMP MIB module HOST-RESOURCES-TYPES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HOST-RESOURCES-TYPES
# Produced by pysmi-0.3.4 at Wed May  1 13:32:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hrStorage, hrMIBAdminInfo, hrDevice = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorage", "hrMIBAdminInfo", "hrDevice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Bits, Integer32, Counter64, IpAddress, MibIdentifier, ModuleIdentity, Gauge32, Unsigned32, ObjectIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Bits", "Integer32", "Counter64", "IpAddress", "MibIdentifier", "ModuleIdentity", "Gauge32", "Unsigned32", "ObjectIdentity", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hostResourcesTypesModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 25, 7, 4))
hostResourcesTypesModule.setRevisions(('2000-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hostResourcesTypesModule.setRevisionsDescriptions(('The original version of this module, published as RFC 2790.',))
if mibBuilder.loadTexts: hostResourcesTypesModule.setLastUpdated('200003060000Z')
if mibBuilder.loadTexts: hostResourcesTypesModule.setOrganization('IETF Host Resources MIB Working Group')
if mibBuilder.loadTexts: hostResourcesTypesModule.setContactInfo('Steve Waldbusser Postal: Lucent Technologies, Inc. 1213 Innsbruck Dr. Sunnyvale, CA 94089 USA Phone: 650-318-1251 Fax: 650-318-1633 Email: waldbusser@ins.com In addition, the Host Resources MIB mailing list is dedicated to discussion of this MIB. To join the mailing list, send a request message to hostmib-request@andrew.cmu.edu. The mailing list address is hostmib@andrew.cmu.edu.')
if mibBuilder.loadTexts: hostResourcesTypesModule.setDescription('This MIB module registers type definitions for storage types, device types, and file system types. After the initial revision, this module will be maintained by IANA.')
hrStorageTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 25, 2, 1))
hrStorageOther = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 1))
if mibBuilder.loadTexts: hrStorageOther.setStatus('current')
if mibBuilder.loadTexts: hrStorageOther.setDescription('The storage type identifier used when no other defined type is appropriate.')
hrStorageRam = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 2))
if mibBuilder.loadTexts: hrStorageRam.setStatus('current')
if mibBuilder.loadTexts: hrStorageRam.setDescription('The storage type identifier used for RAM.')
hrStorageVirtualMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 3))
if mibBuilder.loadTexts: hrStorageVirtualMemory.setStatus('current')
if mibBuilder.loadTexts: hrStorageVirtualMemory.setDescription('The storage type identifier used for virtual memory, temporary storage of swapped or paged memory.')
hrStorageFixedDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 4))
if mibBuilder.loadTexts: hrStorageFixedDisk.setStatus('current')
if mibBuilder.loadTexts: hrStorageFixedDisk.setDescription('The storage type identifier used for non-removable rigid rotating magnetic storage devices.')
hrStorageRemovableDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 5))
if mibBuilder.loadTexts: hrStorageRemovableDisk.setStatus('current')
if mibBuilder.loadTexts: hrStorageRemovableDisk.setDescription('The storage type identifier used for removable rigid rotating magnetic storage devices.')
hrStorageFloppyDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 6))
if mibBuilder.loadTexts: hrStorageFloppyDisk.setStatus('current')
if mibBuilder.loadTexts: hrStorageFloppyDisk.setDescription('The storage type identifier used for non-rigid rotating magnetic storage devices.')
hrStorageCompactDisc = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 7))
if mibBuilder.loadTexts: hrStorageCompactDisc.setStatus('current')
if mibBuilder.loadTexts: hrStorageCompactDisc.setDescription('The storage type identifier used for read-only rotating optical storage devices.')
hrStorageRamDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 8))
if mibBuilder.loadTexts: hrStorageRamDisk.setStatus('current')
if mibBuilder.loadTexts: hrStorageRamDisk.setDescription('The storage type identifier used for a file system that is stored in RAM.')
hrStorageFlashMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 9))
if mibBuilder.loadTexts: hrStorageFlashMemory.setStatus('current')
if mibBuilder.loadTexts: hrStorageFlashMemory.setDescription('The storage type identifier used for flash memory.')
hrStorageNetworkDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 10))
if mibBuilder.loadTexts: hrStorageNetworkDisk.setStatus('current')
if mibBuilder.loadTexts: hrStorageNetworkDisk.setDescription('The storage type identifier used for a networked file system.')
hrDeviceTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 25, 3, 1))
hrDeviceOther = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 1))
if mibBuilder.loadTexts: hrDeviceOther.setStatus('current')
if mibBuilder.loadTexts: hrDeviceOther.setDescription('The device type identifier used when no other defined type is appropriate.')
hrDeviceUnknown = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 2))
if mibBuilder.loadTexts: hrDeviceUnknown.setStatus('current')
if mibBuilder.loadTexts: hrDeviceUnknown.setDescription('The device type identifier used when the device type is unknown.')
hrDeviceProcessor = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 3))
if mibBuilder.loadTexts: hrDeviceProcessor.setStatus('current')
if mibBuilder.loadTexts: hrDeviceProcessor.setDescription('The device type identifier used for a CPU.')
hrDeviceNetwork = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 4))
if mibBuilder.loadTexts: hrDeviceNetwork.setStatus('current')
if mibBuilder.loadTexts: hrDeviceNetwork.setDescription('The device type identifier used for a network interface.')
hrDevicePrinter = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 5))
if mibBuilder.loadTexts: hrDevicePrinter.setStatus('current')
if mibBuilder.loadTexts: hrDevicePrinter.setDescription('The device type identifier used for a printer.')
hrDeviceDiskStorage = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 6))
if mibBuilder.loadTexts: hrDeviceDiskStorage.setStatus('current')
if mibBuilder.loadTexts: hrDeviceDiskStorage.setDescription('The device type identifier used for a disk drive.')
hrDeviceVideo = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 10))
if mibBuilder.loadTexts: hrDeviceVideo.setStatus('current')
if mibBuilder.loadTexts: hrDeviceVideo.setDescription('The device type identifier used for a video device.')
hrDeviceAudio = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 11))
if mibBuilder.loadTexts: hrDeviceAudio.setStatus('current')
if mibBuilder.loadTexts: hrDeviceAudio.setDescription('The device type identifier used for an audio device.')
hrDeviceCoprocessor = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 12))
if mibBuilder.loadTexts: hrDeviceCoprocessor.setStatus('current')
if mibBuilder.loadTexts: hrDeviceCoprocessor.setDescription('The device type identifier used for a co-processor.')
hrDeviceKeyboard = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 13))
if mibBuilder.loadTexts: hrDeviceKeyboard.setStatus('current')
if mibBuilder.loadTexts: hrDeviceKeyboard.setDescription('The device type identifier used for a keyboard device.')
hrDeviceModem = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 14))
if mibBuilder.loadTexts: hrDeviceModem.setStatus('current')
if mibBuilder.loadTexts: hrDeviceModem.setDescription('The device type identifier used for a modem.')
hrDeviceParallelPort = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 15))
if mibBuilder.loadTexts: hrDeviceParallelPort.setStatus('current')
if mibBuilder.loadTexts: hrDeviceParallelPort.setDescription('The device type identifier used for a parallel port.')
hrDevicePointing = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 16))
if mibBuilder.loadTexts: hrDevicePointing.setStatus('current')
if mibBuilder.loadTexts: hrDevicePointing.setDescription('The device type identifier used for a pointing device (e.g., a mouse).')
hrDeviceSerialPort = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 17))
if mibBuilder.loadTexts: hrDeviceSerialPort.setStatus('current')
if mibBuilder.loadTexts: hrDeviceSerialPort.setDescription('The device type identifier used for a serial port.')
hrDeviceTape = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 18))
if mibBuilder.loadTexts: hrDeviceTape.setStatus('current')
if mibBuilder.loadTexts: hrDeviceTape.setDescription('The device type identifier used for a tape storage device.')
hrDeviceClock = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 19))
if mibBuilder.loadTexts: hrDeviceClock.setStatus('current')
if mibBuilder.loadTexts: hrDeviceClock.setDescription('The device type identifier used for a clock device.')
hrDeviceVolatileMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 20))
if mibBuilder.loadTexts: hrDeviceVolatileMemory.setStatus('current')
if mibBuilder.loadTexts: hrDeviceVolatileMemory.setDescription('The device type identifier used for a volatile memory storage device.')
hrDeviceNonVolatileMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 21))
if mibBuilder.loadTexts: hrDeviceNonVolatileMemory.setStatus('current')
if mibBuilder.loadTexts: hrDeviceNonVolatileMemory.setDescription('The device type identifier used for a non-volatile memory storage device.')
hrFSTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 25, 3, 9))
hrFSOther = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 1))
if mibBuilder.loadTexts: hrFSOther.setStatus('current')
if mibBuilder.loadTexts: hrFSOther.setDescription('The file system type identifier used when no other defined type is appropriate.')
hrFSUnknown = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 2))
if mibBuilder.loadTexts: hrFSUnknown.setStatus('current')
if mibBuilder.loadTexts: hrFSUnknown.setDescription('The file system type identifier used when the type of file system is unknown.')
hrFSBerkeleyFFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 3))
if mibBuilder.loadTexts: hrFSBerkeleyFFS.setStatus('current')
if mibBuilder.loadTexts: hrFSBerkeleyFFS.setDescription('The file system type identifier used for the Berkeley Fast File System.')
hrFSSys5FS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 4))
if mibBuilder.loadTexts: hrFSSys5FS.setStatus('current')
if mibBuilder.loadTexts: hrFSSys5FS.setDescription('The file system type identifier used for the System V File System.')
hrFSFat = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 5))
if mibBuilder.loadTexts: hrFSFat.setStatus('current')
if mibBuilder.loadTexts: hrFSFat.setDescription("The file system type identifier used for DOS's FAT file system.")
hrFSHPFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 6))
if mibBuilder.loadTexts: hrFSHPFS.setStatus('current')
if mibBuilder.loadTexts: hrFSHPFS.setDescription("The file system type identifier used for OS/2's High Performance File System.")
hrFSHFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 7))
if mibBuilder.loadTexts: hrFSHFS.setStatus('current')
if mibBuilder.loadTexts: hrFSHFS.setDescription('The file system type identifier used for the Macintosh Hierarchical File System.')
hrFSMFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 8))
if mibBuilder.loadTexts: hrFSMFS.setStatus('current')
if mibBuilder.loadTexts: hrFSMFS.setDescription('The file system type identifier used for the Macintosh File System.')
hrFSNTFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 9))
if mibBuilder.loadTexts: hrFSNTFS.setStatus('current')
if mibBuilder.loadTexts: hrFSNTFS.setDescription('The file system type identifier used for the Windows NT File System.')
hrFSVNode = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 10))
if mibBuilder.loadTexts: hrFSVNode.setStatus('current')
if mibBuilder.loadTexts: hrFSVNode.setDescription('The file system type identifier used for the VNode File System.')
hrFSJournaled = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 11))
if mibBuilder.loadTexts: hrFSJournaled.setStatus('current')
if mibBuilder.loadTexts: hrFSJournaled.setDescription('The file system type identifier used for the Journaled File System.')
hrFSiso9660 = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 12))
if mibBuilder.loadTexts: hrFSiso9660.setStatus('current')
if mibBuilder.loadTexts: hrFSiso9660.setDescription("The file system type identifier used for the ISO 9660 File System for CD's.")
hrFSRockRidge = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 13))
if mibBuilder.loadTexts: hrFSRockRidge.setStatus('current')
if mibBuilder.loadTexts: hrFSRockRidge.setDescription("The file system type identifier used for the RockRidge File System for CD's.")
hrFSNFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 14))
if mibBuilder.loadTexts: hrFSNFS.setStatus('current')
if mibBuilder.loadTexts: hrFSNFS.setDescription('The file system type identifier used for the NFS File System.')
hrFSNetware = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 15))
if mibBuilder.loadTexts: hrFSNetware.setStatus('current')
if mibBuilder.loadTexts: hrFSNetware.setDescription('The file system type identifier used for the Netware File System.')
hrFSAFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 16))
if mibBuilder.loadTexts: hrFSAFS.setStatus('current')
if mibBuilder.loadTexts: hrFSAFS.setDescription('The file system type identifier used for the Andrew File System.')
hrFSDFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 17))
if mibBuilder.loadTexts: hrFSDFS.setStatus('current')
if mibBuilder.loadTexts: hrFSDFS.setDescription('The file system type identifier used for the OSF DCE Distributed File System.')
hrFSAppleshare = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 18))
if mibBuilder.loadTexts: hrFSAppleshare.setStatus('current')
if mibBuilder.loadTexts: hrFSAppleshare.setDescription('The file system type identifier used for the AppleShare File System.')
hrFSRFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 19))
if mibBuilder.loadTexts: hrFSRFS.setStatus('current')
if mibBuilder.loadTexts: hrFSRFS.setDescription('The file system type identifier used for the RFS File System.')
hrFSDGCFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 20))
if mibBuilder.loadTexts: hrFSDGCFS.setStatus('current')
if mibBuilder.loadTexts: hrFSDGCFS.setDescription('The file system type identifier used for the Data General DGCFS.')
hrFSBFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 21))
if mibBuilder.loadTexts: hrFSBFS.setStatus('current')
if mibBuilder.loadTexts: hrFSBFS.setDescription('The file system type identifier used for the SVR4 Boot File System.')
hrFSFAT32 = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 22))
if mibBuilder.loadTexts: hrFSFAT32.setStatus('current')
if mibBuilder.loadTexts: hrFSFAT32.setDescription('The file system type identifier used for the Windows FAT32 File System.')
hrFSLinuxExt2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 23))
if mibBuilder.loadTexts: hrFSLinuxExt2.setStatus('current')
if mibBuilder.loadTexts: hrFSLinuxExt2.setDescription('The file system type identifier used for the Linux EXT2 File System.')
mibBuilder.exportSymbols("HOST-RESOURCES-TYPES", hrDeviceUnknown=hrDeviceUnknown, hrDeviceAudio=hrDeviceAudio, hrStorageNetworkDisk=hrStorageNetworkDisk, hrDeviceCoprocessor=hrDeviceCoprocessor, hrFSFAT32=hrFSFAT32, hrStorageRemovableDisk=hrStorageRemovableDisk, hrFSNetware=hrFSNetware, hrDeviceSerialPort=hrDeviceSerialPort, hrFSBerkeleyFFS=hrFSBerkeleyFFS, hrFSDFS=hrFSDFS, hrFSiso9660=hrFSiso9660, PYSNMP_MODULE_ID=hostResourcesTypesModule, hrFSHFS=hrFSHFS, hrStorageOther=hrStorageOther, hrStorageFloppyDisk=hrStorageFloppyDisk, hrStorageRamDisk=hrStorageRamDisk, hrStorageFixedDisk=hrStorageFixedDisk, hrStorageVirtualMemory=hrStorageVirtualMemory, hrDevicePrinter=hrDevicePrinter, hrDeviceTape=hrDeviceTape, hrDevicePointing=hrDevicePointing, hrStorageCompactDisc=hrStorageCompactDisc, hrDeviceModem=hrDeviceModem, hrDeviceKeyboard=hrDeviceKeyboard, hrStorageRam=hrStorageRam, hrFSVNode=hrFSVNode, hrFSNTFS=hrFSNTFS, hrFSTypes=hrFSTypes, hrFSMFS=hrFSMFS, hrDeviceVideo=hrDeviceVideo, hrFSNFS=hrFSNFS, hrStorageFlashMemory=hrStorageFlashMemory, hrFSAppleshare=hrFSAppleshare, hostResourcesTypesModule=hostResourcesTypesModule, hrDeviceTypes=hrDeviceTypes, hrFSLinuxExt2=hrFSLinuxExt2, hrFSHPFS=hrFSHPFS, hrDeviceClock=hrDeviceClock, hrDeviceNonVolatileMemory=hrDeviceNonVolatileMemory, hrFSJournaled=hrFSJournaled, hrDeviceProcessor=hrDeviceProcessor, hrDeviceDiskStorage=hrDeviceDiskStorage, hrFSSys5FS=hrFSSys5FS, hrFSRockRidge=hrFSRockRidge, hrFSFat=hrFSFat, hrDeviceOther=hrDeviceOther, hrFSAFS=hrFSAFS, hrFSRFS=hrFSRFS, hrFSUnknown=hrFSUnknown, hrFSOther=hrFSOther, hrDeviceVolatileMemory=hrDeviceVolatileMemory, hrFSDGCFS=hrFSDGCFS, hrDeviceParallelPort=hrDeviceParallelPort, hrDeviceNetwork=hrDeviceNetwork, hrStorageTypes=hrStorageTypes, hrFSBFS=hrFSBFS)
