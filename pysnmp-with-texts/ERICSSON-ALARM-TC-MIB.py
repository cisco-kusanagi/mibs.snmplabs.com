#
# PySNMP MIB module ERICSSON-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERICSSON-ALARM-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, TimeTicks, Counter64, Counter32, Unsigned32, ObjectIdentity, Integer32, NotificationType, iso, MibIdentifier, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "TimeTicks", "Counter64", "Counter32", "Unsigned32", "ObjectIdentity", "Integer32", "NotificationType", "iso", "MibIdentifier", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericssonAlarmTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 3))
ericssonAlarmTCMIB.setRevisions(('2008-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ericssonAlarmTCMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setOrganization('Ericsson AB')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setContactInfo('Email: snmp.mib.contact@ericsson.com ')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setDescription('This MIB defines textual conventions used by the ERICSSON-ALARM-MIB. See also Documentation and Use of the Ericsson SNMP Fault Management MIB, Document number EAB/OP-07:0139. Document number: 3/196 03-CXC 172 7549, Rev A')
class EriAlarmType(TextualConvention, Unsigned32):
    description = 'A unique identification of the fault, not including the managed object. Alarm types are used to identify if alarms indicate the same problem or not, for lookup into external alarm documentation, etc. A unique alarm type is identified using the combination of two instances of EriAlarmType. Different managed object types and instances can share alarm types. But if the same managed object reports the same alarm type, it is to be considered to be the same alarm state. The alarm type is a simplification of the different X.733 and 3GPP alarm IRP alarm correlation mechanisms based on EventType, ProbableCause, SpecificProblem and NotificationId.'
    status = 'current'
    displayHint = 'd'

class EriAlarmIndex(TextualConvention, Unsigned32):
    description = 'Index used in the active alarm table. A row shall never change its index during the lifetime of the entry; for example renumbering entries is not allowed when entries are deleted. Renumbering after an agent restart is allowed. Note that this index shall not be used to identify alarms when performing resynchronization, etc. The logical identity for an alarm instance is the managed object and alarm type.'
    status = 'current'
    displayHint = 'd'

class EriAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString'
    description = 'The string used in additional text notifications. This MUST contain enough information for an operator to be able to understand the problem. If this string contains structure, this format should be clearly documented for programs to be able to parse that information. This is a small size range in order to guarantee delivery of notifications without fragmentation. There is a corresponding textual convention, EriLargeAdditionalText, to be used for scalar and columnar objects. The string should adhere to the rules for SnmpAdminString of SNMPv3 framework MIBs.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 256)

class EriLargeAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString'
    description = 'The string used in additional text. This MUST contain enough information for an operator to be able to understand the problem. If this string contains structure, this format should be clearly documented for programs to be able to parse that information. This is a large additional text to be used in tables. There is a corresponding textual convention to be used in alarm notifications, EriAdditionalText. The string should adhere to the rules for SnmpAdminString of SNMPv3 framework MIBs.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 512)

class EriAlarmSpecificProblem(TextualConvention, OctetString):
    description = 'Unique string for the Alarm Type. No different alarm types may share specific problem. Specific Problem and Alarm Type have a one-to-one correspondance.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 64)

class EriAlarmSequenceNumber(TextualConvention, Unsigned32):
    description = 'This is a monotonically increasing counter. It is increased every time a notification is sent. The value is NOT increased for heartbeat notifications. It is carried as a varbind in the alarm notifications as well as in the heartbeat notifications. Management systems can use these varbinds to detect lost notifications.'
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("ERICSSON-ALARM-TC-MIB", PYSNMP_MODULE_ID=ericssonAlarmTCMIB, ericssonAlarmTCMIB=ericssonAlarmTCMIB, EriAlarmSpecificProblem=EriAlarmSpecificProblem, EriAlarmIndex=EriAlarmIndex, EriAdditionalText=EriAdditionalText, EriAlarmSequenceNumber=EriAlarmSequenceNumber, EriAlarmType=EriAlarmType, EriLargeAdditionalText=EriLargeAdditionalText)
