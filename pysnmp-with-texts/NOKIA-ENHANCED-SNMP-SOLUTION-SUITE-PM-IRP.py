#
# PySNMP MIB module NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP
# Produced by pysmi-0.3.4 at Wed May  1 14:23:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NoiAdditionalText, NoiEventTime, NoiAlarmTableCount = mibBuilder.importSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION", "NoiAdditionalText", "NoiEventTime", "NoiAlarmTableCount")
NoiMeasurementJobStatus, NoiMeasurementResultTransfer, NoiMeasurementResultIdentifier, NoiMeasurementFileTransfer, NoiMeasurementFileName, NoiMeasurementActivationError, NoiMeasurementFileDirectory = mibBuilder.importSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION", "NoiMeasurementJobStatus", "NoiMeasurementResultTransfer", "NoiMeasurementResultIdentifier", "NoiMeasurementFileTransfer", "NoiMeasurementFileName", "NoiMeasurementActivationError", "NoiMeasurementFileDirectory")
noiPmTable, noiPmCompliance, noiPmVariable, noiOpenInterfaceModule, noiPmNotification = mibBuilder.importSymbols("NOKIA-NE3S-REGISTRATION-MIB", "noiPmTable", "noiPmCompliance", "noiPmVariable", "noiOpenInterfaceModule", "noiPmNotification")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ModuleIdentity, NotificationType, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ObjectIdentity, Counter32, Counter64, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "NotificationType", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
noiSnmpPmIrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 4))
noiSnmpPmIrp.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: noiSnmpPmIrp.setRevisionsDescriptions(('Version 1.0.6',))
if mibBuilder.loadTexts: noiSnmpPmIrp.setLastUpdated('200227020000Z')
if mibBuilder.loadTexts: noiSnmpPmIrp.setOrganization('Nokia Networks')
if mibBuilder.loadTexts: noiSnmpPmIrp.setContactInfo('e-mail: NET-OSS-OPEN-SNMP DL (Microsoft Outlook, Nokia internal) DL.NET-OSS-OPEN-SNMP-DL@nokia.com')
if mibBuilder.loadTexts: noiSnmpPmIrp.setDescription('This SNMP MIB-module specifies the SNMP Solution Set of the PM Integration Reference Point (IRP) also known as Enhanced SNMP Solution Suite. The purpose of this IRP is to define an interface though which a network element manager or a network element) can communicate PM information for its managed objects to Nokia OS, NetAct.')
noiPmIrpVersion = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmIrpVersion.setStatus('current')
if mibBuilder.loadTexts: noiPmIrpVersion.setDescription("This object represents the version of the PM IRP supported by the agent. The format is 'n.m,o', where 'n' is the main version number of the interface model and 'm' and 'o' the release number within the main version. This version is 1.0.6")
noiPmFileTransferProtocol = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 2), NoiMeasurementFileTransfer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiPmFileTransferProtocol.setStatus('current')
if mibBuilder.loadTexts: noiPmFileTransferProtocol.setDescription('Contains the supported file transfer mechanism for various files within NE3S. NetAct does not modify this object, but it shall be the responsibility of the agent to set the appropriate values. From a NetAct perspective, this object is treated as it would be specified as read-only. The object has been declared as read-write, to allow for instance configuring this value by an EM.')
noiPmResultTransfer = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 3), NoiMeasurementResultTransfer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiPmResultTransfer.setStatus('current')
if mibBuilder.loadTexts: noiPmResultTransfer.setDescription('Contains the supported transfer mechanism for measurement result, e.g. notification based or polling based. NetAct does not modify this object, but it shall be the responsibility of the agent to set the appropriate values. From a NetAct perspective, this object is treated as it would be specified as read-only. The object has been declared as read-write, to allow for instance configuring this value by an EM.')
noiMeasurementScheduleFileDirectory = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 4), NoiMeasurementFileDirectory()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementScheduleFileDirectory.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementScheduleFileDirectory.setDescription('Contains the directory where the measurement schedule file is stored within the agent. The manager polls the value before downloading the measurement file. NetAct does not modify this object, but it shall be the responsibility of the agent to set the appropriate values. From a NetAct perspective, this object is treated as it would be specified as read-only. The object has been declared as read-write, to allow for instance configuring this value by an EM.')
noiMeasurementRepositoryDirectory = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 5), NoiMeasurementFileDirectory()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementRepositoryDirectory.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementRepositoryDirectory.setDescription('Contains the directory where the measurement repository file is stored within the agent. The manager polls the value before retrieving the repository file. NetAct does not modify this object, but it shall be the responsibility of the agent to set the appropriate values. From a NetAct perspective, this object is treated as it would be specified as read-only. The object has been declared as read-write, to allow for instance configuring this value by an EM.')
noiMeasurementRepositoryFile = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 6), NoiMeasurementFileName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementRepositoryFile.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementRepositoryFile.setDescription('Contains the file name of the repository file. The manager polls the value before retrieving the repository file. NetAct does not modify this object, but it shall be the responsibility of the agent to set the appropriate values. From a NetAct perspective, this object is treated as it would be specified as read-only. The object has been declared as read-write, to allow for instance configuring this value by an EM.')
noiMeasurementJobStatus = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 7), NoiMeasurementJobStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementJobStatus.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementJobStatus.setDescription('This object represent the measurement job status. The agent will update the value according to the state model defined in the interface specification.')
noiMeasurementActivationError = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 8), NoiMeasurementActivationError()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementActivationError.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementActivationError.setDescription('Contains the error code in case of failure in measurement administration.')
noiPmAdditionalText = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 9), NoiAdditionalText()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmAdditionalText.setStatus('current')
if mibBuilder.loadTexts: noiPmAdditionalText.setDescription('Contains additional text and is used in conjunction with the notification noiMeasurementResultTableRebuild and in case of failure in measurement administration.')
noiPmFileStoringPeriod = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiPmFileStoringPeriod.setStatus('current')
if mibBuilder.loadTexts: noiPmFileStoringPeriod.setDescription(' Contains the storage duraion for the measurement file in the agent. Duration in minutes. NetAct does not modify this object, but it shall be the responsibility of the agent to set the appropriate values. From a NetAct perspective, this object is treated as it would be specified as read-only. The object has been declared as read-write, to allow for instance configuring this value by an EM.')
noiMeasurementResultTableCount = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 1), NoiAlarmTableCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementResultTableCount.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementResultTableCount.setDescription('Contains the number or current active entries in the measurement table. When the table is empty, the value of this object is zero (0).')
noiMeasurementResultTableMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 2), NoiAlarmTableCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementResultTableMaxCount.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementResultTableMaxCount.setDescription('Contains the maximum number of entries in the in the measurement table.')
noiPmLastMeasurementResultId = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 3), NoiMeasurementResultIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmLastMeasurementResultId.setStatus('current')
if mibBuilder.loadTexts: noiPmLastMeasurementResultId.setDescription('This object represent the measurement identifier of last send notification noiMeasurementResultReady The manager can retrieve the current value of this object to detect lost notifications. This mechanism can be used by the manager when no notification is received for a certain time (e.g. 30 minutes) to evaluate whether an retrieval of of entries from the measurement table shall be performed')
noiMeasurementResultTable = MibTable((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4), )
if mibBuilder.loadTexts: noiMeasurementResultTable.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementResultTable.setDescription('Table containing information about the measurement files that are currently stored in the Network Element and accessible for the manager. Agent will create a new entry, whenever a new measurement file has been created. When removing a measurement file, the corresponding entry in the table must be removed.')
noiMeasurementResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1), ).setIndexNames((0, "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"))
if mibBuilder.loadTexts: noiMeasurementResultEntry.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementResultEntry.setDescription('One entry in the measurement table, containing the information of one measurement file.')
noiMeasurementResultIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 1), NoiMeasurementResultIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementResultIdentifier.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementResultIdentifier.setDescription('This object represents the measurement identifier of an entry in the measurement table. It uniquely identifies an entry in the table.')
noiMeasurementFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 2), NoiMeasurementFileName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementFileName.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementFileName.setDescription('This object represents the file name of a measurement result file.')
noiMeasurementFileDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 3), NoiMeasurementFileDirectory()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementFileDirectory.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementFileDirectory.setDescription('This object represents the full path of a measurement resulta file.')
noiPmEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 4), NoiEventTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmEventTime.setStatus('current')
if mibBuilder.loadTexts: noiPmEventTime.setDescription('This object represents the time the event occured.')
noiMeasurementResultReady = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 3, 3, 0, 1)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileDirectory"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileName"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"))
if mibBuilder.loadTexts: noiMeasurementResultReady.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementResultReady.setDescription('This notification is used when a new measurement data file has been created and a new entry in the measurement table has been inserted.')
noiMeasurementResultTableRebuild = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 3, 3, 0, 2)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"))
if mibBuilder.loadTexts: noiMeasurementResultTableRebuild.setStatus('current')
if mibBuilder.loadTexts: noiMeasurementResultTableRebuild.setDescription('This notification is used when the measurement table in the agent has been rebuild. The notification will be emitted after the measurement table has been dropped and all previously stored entries have been removed')
noiPmIRPCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 1)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmMandatoryGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmNotificationOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiPmIRPCompliance = noiPmIRPCompliance.setStatus('current')
if mibBuilder.loadTexts: noiPmIRPCompliance.setDescription('This specifies the objects that are required to claim compliance to NE3S PM Fragment.')
noiPmMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 2)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmIrpVersion"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmLastMeasurementResultId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementScheduleFileDirectory"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableCount"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableMaxCount"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileDirectory"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileName"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmFileStoringPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiPmMandatoryGroup = noiPmMandatoryGroup.setStatus('current')
if mibBuilder.loadTexts: noiPmMandatoryGroup.setDescription('A collection of objects that represents mandatory PM attributes.')
noiPmNotificationOptionalGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 3)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultReady"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableRebuild"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiPmNotificationOptionalGroup = noiPmNotificationOptionalGroup.setStatus('current')
if mibBuilder.loadTexts: noiPmNotificationOptionalGroup.setDescription('A collection of optional measurement notifications.')
mibBuilder.exportSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", noiPmMandatoryGroup=noiPmMandatoryGroup, noiMeasurementResultIdentifier=noiMeasurementResultIdentifier, noiSnmpPmIrp=noiSnmpPmIrp, noiMeasurementFileDirectory=noiMeasurementFileDirectory, noiMeasurementResultTableCount=noiMeasurementResultTableCount, noiPmIrpVersion=noiPmIrpVersion, noiPmNotificationOptionalGroup=noiPmNotificationOptionalGroup, noiMeasurementJobStatus=noiMeasurementJobStatus, noiMeasurementFileName=noiMeasurementFileName, noiMeasurementResultTableRebuild=noiMeasurementResultTableRebuild, noiPmEventTime=noiPmEventTime, noiPmLastMeasurementResultId=noiPmLastMeasurementResultId, noiMeasurementResultEntry=noiMeasurementResultEntry, noiPmResultTransfer=noiPmResultTransfer, noiPmFileStoringPeriod=noiPmFileStoringPeriod, noiMeasurementActivationError=noiMeasurementActivationError, noiPmAdditionalText=noiPmAdditionalText, noiMeasurementResultTable=noiMeasurementResultTable, noiMeasurementScheduleFileDirectory=noiMeasurementScheduleFileDirectory, noiMeasurementRepositoryDirectory=noiMeasurementRepositoryDirectory, noiMeasurementResultReady=noiMeasurementResultReady, noiMeasurementRepositoryFile=noiMeasurementRepositoryFile, noiMeasurementResultTableMaxCount=noiMeasurementResultTableMaxCount, noiPmIRPCompliance=noiPmIRPCompliance, noiPmFileTransferProtocol=noiPmFileTransferProtocol, PYSNMP_MODULE_ID=noiSnmpPmIrp)
