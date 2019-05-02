#
# PySNMP MIB module HP-MPE-XL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-MPE-XL
# Produced by pysmi-0.3.4 at Wed May  1 13:36:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
Timeticks, = mibBuilder.importSymbols("RFC1155-SMI", "Timeticks")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Counter64, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, TimeTicks, ObjectIdentity, Counter32, MibIdentifier, Unsigned32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter64", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "TimeTicks", "ObjectIdentity", "Counter32", "MibIdentifier", "Unsigned32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3))
general = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 1))
mpeXLSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3))
volume = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1))
processor = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2))
volumeMounted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeMounted.setStatus('mandatory')
if mibBuilder.loadTexts: volumeMounted.setDescription('The number of volumes that are currently mounted on the system.')
volumeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2), )
if mibBuilder.loadTexts: volumeTable.setStatus('mandatory')
if mibBuilder.loadTexts: volumeTable.setDescription('Volume table')
volumeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1), ).setIndexNames((0, "HP-MPE-XL", "volumeName"))
if mibBuilder.loadTexts: volumeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: volumeEntry.setDescription('Each entry contains objects that define the volume.')
volumeLDEV = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeLDEV.setStatus('mandatory')
if mibBuilder.loadTexts: volumeLDEV.setDescription('The logical device number for the volume.')
volumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeName.setStatus('mandatory')
if mibBuilder.loadTexts: volumeName.setDescription('This is the volume set name combined with the member name that uniquely distinguishes the actual volume on the system.')
volumeDriveType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeDriveType.setStatus('mandatory')
if mibBuilder.loadTexts: volumeDriveType.setDescription('The type of the actual hardware device, e.g. HP7935.')
volumeSectorSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeSectorSize.setStatus('mandatory')
if mibBuilder.loadTexts: volumeSectorSize.setDescription('The logical sector size of the volume in bytes')
volumeType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("system", 1), ("nonSystem", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeType.setStatus('mandatory')
if mibBuilder.loadTexts: volumeType.setDescription('The type of volume set.')
volumeCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: volumeCapacity.setDescription('The capacity of the volume in sectors.')
volumeMPEOverhead = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeMPEOverhead.setStatus('mandatory')
if mibBuilder.loadTexts: volumeMPEOverhead.setDescription('The total overhead which consists of everything on a volume that is not set aside for file space use. This includes volume label, file label table, directory, volume set information table, free space map, transient space, and transaction management overhead.')
volumeMPETransOverhead = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeMPETransOverhead.setStatus('mandatory')
if mibBuilder.loadTexts: volumeMPETransOverhead.setDescription('The total MPE XL transient space overhead for the volume.')
volumeMPEConfigMaxTrans = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeMPEConfigMaxTrans.setStatus('mandatory')
if mibBuilder.loadTexts: volumeMPEConfigMaxTrans.setDescription('The configured maximum transient space for the volume.')
volumeDirSpaceOverhead = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeDirSpaceOverhead.setStatus('mandatory')
if mibBuilder.loadTexts: volumeDirSpaceOverhead.setDescription('The directory space overhead that is reserved for accounting information.')
volumeFileLabelOverhead = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeFileLabelOverhead.setStatus('mandatory')
if mibBuilder.loadTexts: volumeFileLabelOverhead.setDescription('The file label overhead for this volume.')
volumeTransactionMgmtOverhead = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeTransactionMgmtOverhead.setStatus('mandatory')
if mibBuilder.loadTexts: volumeTransactionMgmtOverhead.setDescription('The transaction management overhead for this volume.')
volumeSpoolFileDiscUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeSpoolFileDiscUsage.setStatus('mandatory')
if mibBuilder.loadTexts: volumeSpoolFileDiscUsage.setDescription('The spool file disc space usage which consists of the volume space that is used by hidden spool files that are not part of the permanent file space.')
volumePermFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumePermFiles.setStatus('mandatory')
if mibBuilder.loadTexts: volumePermFiles.setDescription('The space used for permanent files on this volume.')
volumeTempFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeTempFiles.setStatus('mandatory')
if mibBuilder.loadTexts: volumeTempFiles.setDescription('The space used for temporary files on this volume.')
volumeTotalFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeTotalFreeSpace.setStatus('mandatory')
if mibBuilder.loadTexts: volumeTotalFreeSpace.setDescription('The total free space for the volume.')
volumeLargestContigFree = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeLargestContigFree.setStatus('mandatory')
if mibBuilder.loadTexts: volumeLargestContigFree.setDescription('The largest contiguous free space area on the volume.')
volumePercentUtilized = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumePercentUtilized.setStatus('mandatory')
if mibBuilder.loadTexts: volumePercentUtilized.setDescription('The percent of the volume currently being used for file storage and operating system overhead.')
numActive = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numActive.setStatus('mandatory')
if mibBuilder.loadTexts: numActive.setDescription('Number of processors currently active, in the system. A processor is considered active if it is capable of begin dispatched.')
numPresent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numPresent.setStatus('mandatory')
if mibBuilder.loadTexts: numPresent.setDescription('The number of processors physically present in the system.')
processorMIstate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: processorMIstate.setStatus('mandatory')
if mibBuilder.loadTexts: processorMIstate.setDescription('Setting this object to 1 will result in the measurement interface being turned on for the global processor statistics which will increase the amount of CPU used by the SNMP/XL Agent. Setting this object to 0 will cause the measurement interface to be disabled for the global processor statistics. When the measurement interface is enabled, the cpuUtilization object described below may be obtained.')
cpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilization.setStatus('mandatory')
if mibBuilder.loadTexts: cpuUtilization.setDescription('The overall CPU utilization percentage on the system. If the system has more than one processor, the value returned is averaged out over all of the processors that are present. The measurement interface must be enabled in order to get a valid value returned for this object ( see above object ). The number returned is the percentage of the CPU that was used since the last time the number was sampled. This value is consistent with various HP performance tools such as Glance/XL. If the measurement interface is not enabled, the value returned will be 0.')
mibBuilder.exportSymbols("HP-MPE-XL", numActive=numActive, volumePermFiles=volumePermFiles, nm=nm, volumeDriveType=volumeDriveType, volumeFileLabelOverhead=volumeFileLabelOverhead, volumeSpoolFileDiscUsage=volumeSpoolFileDiscUsage, volumeName=volumeName, volumeMPETransOverhead=volumeMPETransOverhead, mpeXLSystem=mpeXLSystem, volumeLargestContigFree=volumeLargestContigFree, volumeCapacity=volumeCapacity, hp=hp, general=general, system=system, processor=processor, volumeTransactionMgmtOverhead=volumeTransactionMgmtOverhead, numPresent=numPresent, volumeLDEV=volumeLDEV, volumeTable=volumeTable, volumePercentUtilized=volumePercentUtilized, volumeSectorSize=volumeSectorSize, processorMIstate=processorMIstate, volumeTotalFreeSpace=volumeTotalFreeSpace, volumeMounted=volumeMounted, volumeEntry=volumeEntry, volumeMPEConfigMaxTrans=volumeMPEConfigMaxTrans, volumeDirSpaceOverhead=volumeDirSpaceOverhead, volumeTempFiles=volumeTempFiles, cpuUtilization=cpuUtilization, volume=volume, volumeMPEOverhead=volumeMPEOverhead, volumeType=volumeType)
