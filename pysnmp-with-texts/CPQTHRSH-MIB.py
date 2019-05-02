#
# PySNMP MIB module CPQTHRSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQTHRSH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
compaq, cpqHoTrapFlags = mibBuilder.importSymbols("CPQHOST-MIB", "compaq", "cpqHoTrapFlags")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
TimeTicks, Counter64, enterprises, ModuleIdentity, Counter32, NotificationType, IpAddress, MibIdentifier, ObjectIdentity, Gauge32, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "enterprises", "ModuleIdentity", "Counter32", "NotificationType", "IpAddress", "MibIdentifier", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpqThresholdMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 10))
cpqMeMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 10, 1))
cpqMeComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 10, 2))
cpqMeInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 10, 2, 1))
cpqMeAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 10, 2, 2))
cpqMeOsCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4))
cpqMeMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 232, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeMibRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeMibRevMajor.setDescription('The Major Revision level of the MIB. A change in the major revision level represents a major change in the architecture of the MIB. A change in the major revision level may indicate a significant change in the information supported and/or the meaning of the supported information, correct interpretation of data may require a MIB document with the same major revision level.')
cpqMeMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 232, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeMibRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeMibRevMinor.setDescription('The Minor Revision level of the MIB. A change in the minor revision level may represent some minor additional support, no changes to any pre-existing information has occurred.')
cpqMeMibCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeMibCondition.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeMibCondition.setDescription('The overall condition. This object represents the overall status of the threshold management system represented by this MIB.')
cpqMeOsCommonPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeOsCommonPollFreq.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeOsCommonPollFreq.setDescription("The Insight Agent's minimum polling frequency. The minimum frequency, in seconds, at which the Insight Agent will permit the cpqMeAlarmInterval to be SET (for an entry in the cpqMeAlarm table). Changing this variable to smaller values will allow a management station to modify or add entries in the cpqMeAlarm table that can have smaller cpqMeAlarmInterval values and will therefore be polled more frequently. An agent may also choose to fail any request to change the poll frequency to a value that would severely impact system performance.")
cpqMeOsCommonModuleTable = MibTable((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2), )
if mibBuilder.loadTexts: cpqMeOsCommonModuleTable.setStatus('deprecated')
if mibBuilder.loadTexts: cpqMeOsCommonModuleTable.setDescription('A table of software modules that provide an interface to the device this MIB describes.')
cpqMeOsCommonModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1), ).setIndexNames((0, "CPQTHRSH-MIB", "cpqMeOsCommonModuleIndex"))
if mibBuilder.loadTexts: cpqMeOsCommonModuleEntry.setStatus('deprecated')
if mibBuilder.loadTexts: cpqMeOsCommonModuleEntry.setDescription('A description of a software modules that provide an interface to the device this MIB describes.')
cpqMeOsCommonModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeOsCommonModuleIndex.setStatus('deprecated')
if mibBuilder.loadTexts: cpqMeOsCommonModuleIndex.setDescription('A unique index for this module description.')
cpqMeOsCommonModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeOsCommonModuleName.setStatus('deprecated')
if mibBuilder.loadTexts: cpqMeOsCommonModuleName.setDescription('The module name.')
cpqMeOsCommonModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeOsCommonModuleVersion.setStatus('deprecated')
if mibBuilder.loadTexts: cpqMeOsCommonModuleVersion.setDescription('The module version in XX.YY format. Where XX is the major version number and YY is the minor version number. This field will be a null (size 0) string if the agent cannot provide the module version.')
cpqMeOsCommonModuleDate = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeOsCommonModuleDate.setStatus('deprecated')
if mibBuilder.loadTexts: cpqMeOsCommonModuleDate.setDescription('The module date. field octets contents range ===== ====== ======= ===== 1 1-2 year 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minute 0..59 6 7 second 0..60 (use 60 for leap-second) This field will be set to year = 0 if the agent cannot provide the module date. The hour, minute, and second field will be set to zero (0) if they are not relevant. The year field is set with the most significant octet first.')
cpqMeOsCommonModulePurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeOsCommonModulePurpose.setStatus('deprecated')
if mibBuilder.loadTexts: cpqMeOsCommonModulePurpose.setDescription('The purpose of the module described in this entry.')
cpqMeAlarmNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeAlarmNextIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmNextIndex.setDescription('The index of the next available entry in the cpqMeAlarm table. If the maximum number of entries to the cpqMeAlarm table has been reached, this index will contain -1.')
cpqMeAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2), )
if mibBuilder.loadTexts: cpqMeAlarmTable.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmTable.setDescription('A list of alarm entries.')
cpqMeAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1), ).setIndexNames((0, "CPQTHRSH-MIB", "cpqMeAlarmIndex"))
if mibBuilder.loadTexts: cpqMeAlarmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmEntry.setDescription('A list of parameters that set up a periodic checking for alarm conditions.')
cpqMeAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeAlarmIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmIndex.setDescription('An index that uniquely identifies an entry in the cpqMeAlarm table. Each such entry defines a diagnostic sample at a particular interval for an object on the device.')
cpqMeAlarmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmInterval.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmInterval.setDescription('The interval, in seconds, between consecutive samples of the data. When setting this variable, care should be given to ensure that the variable being monitored will not exceed 2^31 - 1 and roll over. The first sample will be taken immediately upon the cpqMeAlarmStatus being set to valid(1). This object may not be modified if the associated cpqMeAlarmStatus object is equal to valid(1).')
cpqMeAlarmVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmVariable.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmVariable.setDescription('The object identifier of the particular variable to be sampled. Only variables that resolve to an ASN.1 primitive type of INTEGER (INTEGER, Counter, Gauge, or TimeTicks) may be sampled. Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view. Because there is thus no acceptable means of restricting the read access that could be obtained through the alarm mechanism, the agent must only grant write access to this object in those views that have read access to all objects on the agent. During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned. If at any time the variable name of an established cpqMeAlarmEntry is no longer available in the selected MIB view, the agent must change the status of this cpqMeAlarmEntry to tempUnavailable(5). This object may not be modified if the associated cpqMeAlarmStatus object is equal to valid(1).')
cpqMeAlarmSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("absSuppressRisingTrap", 3), ("absSuppressFallingTrap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmSampleType.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmSampleType.setDescription('The method of sampling the selected variable and calculating the value to be compared against the thresholds. If the sample type (cpqMeAlarmSampleType) is absoluteValue(1), the most recent sampled value of the selected variable (cpqMeAlarmVariable) will be compared directly with the thresholds (cpqMeAlarmRisingThreshold and cpqMeAlarmFallingThreshold). If the sample type (cpqMeAlarmSampleType) is deltaValue(2), the most recently sampled value minus the previous sampled value is compared with the threshold values (cpqMeAlarmRisingThreshold and cpqMeAlarmFallingThreshold). If the sample type is absSupressRisingValue(3), only comparisons with the cpqMeAlarmFallingThreshold are performed. If the sample type is absSupressFallingValue(4), only comparisons with the cpqMeAlarmRisingThreshold are performed. This object may not be modified if the associated cpqMeAlarmStatus object is equal to valid(1).')
cpqMeAlarmValue = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqMeAlarmValue.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmValue.setDescription('The value of the object identifier (cpqMeAlarmVariable) during the last sampling period. The value during the current sampling period is not made available until the period is completed. If the sample type (cpqMeAlarmSampleType) is absoluteValue(1), absSupressRisingValue(3), or absSupressFallingValue(4), the value (cpqMeAlarmValue) should become the actual value obtained during this sampling period. If the sample type (cpqMeAlarmSampleType) is deltaValue(2), the value (cpqMeAlarmValue) should become the most recently sampled value minus the previous sample (cpqMeAlarmValue).')
cpqMeAlarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmStartupAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmStartupAlarm.setDescription('The alarm that may be sent when this entry is first set to valid. If the sample type (cpqMeAlarmSampleType) is absoluteValue(1), then the following comparisons are used to generate an event. If cpqMeAlarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3), then a single event will be generated if the first sample after this entry becomes valid is greater than or equal to this threshold. If cpqMeAlarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3), then a single event will be generated if the first sample after this entry becomes valid is less than or equal to this threshold. This object may not be modified if the associated cpqMeAlarmStatus object is equal to valid(1).')
cpqMeAlarmRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmRisingThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmRisingThreshold.setDescription('A threshold for the sampled object identifier (cpqMeAlarmVariable). If the sample type (cpqMeAlarmSampleType) is absoluteValue(1), then the following describes the comparison. When the current sampled value is greater than or equal to this threshold, and the value (cpqMeAlarmValue) at the last sampling interval was less than this threshold, a single event will be generated. If cpqMeAlarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3), then a single event will be generated if the first sample after this entry becomes valid is greater than or equal to this threshold. After a rising event is generated, another such event will not be generated until the sampled value falls below this threshold and reaches the falling threshold (cpaMeAlarmFallingThreshold). If the sample type (cpqMeAlarmSampleType) is deltaValue(2), then the following describes the comparison. When the most recently sampled value minus the previous sampled value is greater than or equal to the threshold (cpqMeAlarmRisingThreshold), and the current alarm value (cpqMeAlarmValue) is less than the threshold value (cpqMeAlarmRisingThreshold) a single event will be generated. After a rising event is generated, another such event will not be generated until the most recently sampled value minus the previous sampled value falls below this threshold (cpqMeAlarmRisingThreshold) and reaches the falling threshold (cpqMeAlarmFallingThreshold). This object may not be modified if the associated cpqMeAlarmStatus object is equal to valid(1).')
cpqMeAlarmFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmFallingThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmFallingThreshold.setDescription('A threshold for the sampled object identifier (cpqMeAlarmVariable). If the sample type (cpqMeAlarmSampleType) is absoluteValue(1), then the following describes the comparison. When the current sampled value is less than or equal to this threshold, and the value (cpqMeAlarmValue) at the last sampling interval was greater than this threshold, a single event will be generated. If cpqMeAlarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3), then a single event will be generated if the first sample after this entry becomes valid is less than or equal to this threshold. After a falling event is generated, another such event will not be generated until the sampled value rises above this threshold and reaches the rising threshold (cpaMeAlarmRisingThreshold). If the sample type (cpqMeAlarmSampleType) is deltaValue(2), then the following describes the comparison. When the most recently sampled value minus the previous sampled value is less than or equal to the threshold (cpqMeAlarmFallingThreshold), and the current alarm value (cpqMeAlarmValue) is greater than the threshold value (cpqMeAlarmFallingThreshold) a single event will be generated. After a falling event is generated, another such event will not be generated until the most recently sampled value minus the previous sampled value rises above this threshold (cpqMeAlarmFallingThreshold) and reaches the rising threshold (cpqMeAlarmRisingThreshold). This object may not be modified if the associated cpqMeAlarmStatus object is equal to valid(1).')
cpqMeAlarmPermanence = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("temporary", 1), ("permanent", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmPermanence.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmPermanence.setDescription('This specifies if the threshold management software should recreate this entry if it is brought down and then restarted. A temporary entry will not be recreated after a restart. A permanent entry will be recreated after a restart and requires an explicit invalidation to be removed.')
cpqMeAlarmOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmOwner.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmOwner.setDescription("The entity that configured this entry and is therefore using the resources assigned to it. This string is used to model an administratively assigned name of the owner of a resource. This information is taken from the NVT ASCII character set. It is suggested that this name contain one or more of the following: IP address, management station name, network manager's name, location, or phone number. In some cases the agent itself will be the owner of an entry. In these cases, this string shall be set to a string starting with 'monitor'. SNMP access control is articulated entirely in terms of the contents of MIB views; access to a particular SNMP object instance depends only upon its presence or absence in a particular MIB view and never upon its value or the value of related object instances. Thus, objects of this type afford resolution of resource contention only among cooperating managers; they realize no access control function with respect to uncooperative parties.")
cpqMeAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4), ("tempUnavailable", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmStatus.setDescription('The status of this alarm entry. Setting this object to the value invalid(4) has the effect of invalidating the corresponding entry. That is, it effectively disassociates the mapping identified with said entry. It is an implementation-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries currently not in use. Proper interpretation of such entries requires examination of the relevant cpqMeAlarmStatus object. An existing instance of this object cannot be set to createRequest(2). This object may only be set to createRequest(2) when this instance is created. When this object is created, the agent may wish to create supplemental object instances to complete a conceptual row in this table. Immediately after completing the create operation, the agent must set this object to underCreation(3). Entries shall exist in the underCreation(3) state until the management station is finished configuring the entry and sets this object to valid(1) or aborts, setting this object to invalid(4). The agent will deny a request to modify an underCreation(3) entry to be that of createRequest(2) in order to lessen problems arising when multiple management stations may be trying to add an entry with the same index. If the agent determines that an entry has been in the underCreation(3) state for an abnormally long time, it may decide that the management station has crashed. If the agent makes this decision, it may set this object to invalid(4) to reclaim the entry. A prudent agent will understand that the management station may need to wait for human input and will allow for that possibility in its determination of this abnormally long period. If the agent has an entry which is valid(4) and it is unable to query the particular ASN.1 object specified, the agent should set the status to tempUnavailable(5). The agent should continue to query that ASN.1 object, and upon a successful query, the agent should set the status back to valid(4).')
cpqMeAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("minor", 3), ("warning", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmSeverity.setDescription('This is used to correlate the severity of a particular alarm entry. The management console can use this to relate the severity of an alarm entry to the end user.')
cpqMeAlarmExtendedDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqMeAlarmExtendedDescription.setStatus('mandatory')
if mibBuilder.loadTexts: cpqMeAlarmExtendedDescription.setDescription('This string contains meaningful information about the MIB variable which has the threshold set upon it. This information will be bound to a trap and is intended to allow a management console to have specific customized information about the MIB variable which caused the trap.')
cpqMeRisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10001)).setObjects(("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
if mibBuilder.loadTexts: cpqMeRisingAlarm.setDescription('Rising Threshold passed. An alarm entry has crossed its rising threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
cpqMeFallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10002)).setObjects(("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
if mibBuilder.loadTexts: cpqMeFallingAlarm.setDescription('Falling Threshold passed. An alarm entry has crossed its falling threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
cpqMe2RisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10003)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), ("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
if mibBuilder.loadTexts: cpqMe2RisingAlarm.setDescription('Rising Threshold passed. An alarm entry has crossed its rising threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
cpqMe2FallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10004)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), ("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
if mibBuilder.loadTexts: cpqMe2FallingAlarm.setDescription('Falling Threshold passed. An alarm entry has crossed its falling threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
cpqMeRisingAlarmExtended = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10005)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), ("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"), ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"), ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
if mibBuilder.loadTexts: cpqMeRisingAlarmExtended.setDescription('Rising Threshold passed. An alarm entry has crossed its rising threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
cpqMeFallingAlarmExtended = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10006)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), ("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"), ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"), ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
if mibBuilder.loadTexts: cpqMeFallingAlarmExtended.setDescription('Falling Threshold passed. An alarm entry has crossed its falling threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
cpqMeCriticalRisingAlarmExtended = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10007)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), ("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"), ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"), ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
if mibBuilder.loadTexts: cpqMeCriticalRisingAlarmExtended.setDescription('Critical Rising Threshold passed. An alarm entry has crossed its Critical rising threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
cpqMeCriticalFallingAlarmExtended = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,10008)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), ("CPQTHRSH-MIB", "cpqMeAlarmVariable"), ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"), ("CPQTHRSH-MIB", "cpqMeAlarmValue"), ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"), ("CPQTHRSH-MIB", "cpqMeAlarmOwner"), ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"), ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
if mibBuilder.loadTexts: cpqMeCriticalFallingAlarmExtended.setDescription('Critical Falling Threshold passed. An alarm entry has crossed its Critical falling threshold. The instances of those objects contained within the variable list are those of the alarm entry which generated this trap.')
mibBuilder.exportSymbols("CPQTHRSH-MIB", cpqMeAlarmValue=cpqMeAlarmValue, cpqMeOsCommonModuleVersion=cpqMeOsCommonModuleVersion, cpqMeOsCommon=cpqMeOsCommon, cpqMeAlarmStartupAlarm=cpqMeAlarmStartupAlarm, cpqMeAlarmFallingThreshold=cpqMeAlarmFallingThreshold, cpqMeFallingAlarmExtended=cpqMeFallingAlarmExtended, cpqMeMibRevMinor=cpqMeMibRevMinor, cpqMeAlarm=cpqMeAlarm, cpqMeInterface=cpqMeInterface, cpqMeMibRevMajor=cpqMeMibRevMajor, cpqMeAlarmIndex=cpqMeAlarmIndex, cpqMeOsCommonModuleIndex=cpqMeOsCommonModuleIndex, cpqMeCriticalFallingAlarmExtended=cpqMeCriticalFallingAlarmExtended, cpqMeCriticalRisingAlarmExtended=cpqMeCriticalRisingAlarmExtended, cpqMeOsCommonModuleDate=cpqMeOsCommonModuleDate, cpqMeOsCommonPollFreq=cpqMeOsCommonPollFreq, cpqMeOsCommonModulePurpose=cpqMeOsCommonModulePurpose, cpqMeAlarmEntry=cpqMeAlarmEntry, cpqMeOsCommonModuleTable=cpqMeOsCommonModuleTable, cpqMeAlarmVariable=cpqMeAlarmVariable, cpqMeMibRev=cpqMeMibRev, cpqThresholdMgmt=cpqThresholdMgmt, cpqMeRisingAlarmExtended=cpqMeRisingAlarmExtended, cpqMeAlarmSeverity=cpqMeAlarmSeverity, cpqMeRisingAlarm=cpqMeRisingAlarm, cpqMe2RisingAlarm=cpqMe2RisingAlarm, cpqMeOsCommonModuleEntry=cpqMeOsCommonModuleEntry, cpqMeAlarmExtendedDescription=cpqMeAlarmExtendedDescription, cpqMeAlarmRisingThreshold=cpqMeAlarmRisingThreshold, cpqMe2FallingAlarm=cpqMe2FallingAlarm, cpqMeAlarmSampleType=cpqMeAlarmSampleType, cpqMeMibCondition=cpqMeMibCondition, cpqMeAlarmInterval=cpqMeAlarmInterval, cpqMeOsCommonModuleName=cpqMeOsCommonModuleName, cpqMeAlarmNextIndex=cpqMeAlarmNextIndex, cpqMeComponent=cpqMeComponent, cpqMeAlarmTable=cpqMeAlarmTable, cpqMeAlarmOwner=cpqMeAlarmOwner, cpqMeAlarmPermanence=cpqMeAlarmPermanence, cpqMeAlarmStatus=cpqMeAlarmStatus, cpqMeFallingAlarm=cpqMeFallingAlarm)
