#
# PySNMP MIB module TAILF-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TAILF-ALARM-TC-MIB
# Produced by pysmi-0.3.4 at Thu Aug  8 14:21:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.7.0 by user davwang4
# Using Python version 2.7.15 (default, May  1 2018, 16:44:08) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tfModules, = mibBuilder.importSymbols("TAILF-TOP-MIB", "tfModules")
tfAlarmTCModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 24961, 2, 101))
tfAlarmTCModule.setRevisions(('2012-08-30 00:00', '2011-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tfAlarmTCModule.setRevisionsDescriptions(('Released as part of NCS-2.0. Removed TfAlarmType. Fixed DISPLAY-HINT in TfYANGResource and TfUtf8String. Allow TfYANGResource to be an empty string.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: tfAlarmTCModule.setLastUpdated('201208300000Z')
if mibBuilder.loadTexts: tfAlarmTCModule.setOrganization('Tail-f Systems AB')
if mibBuilder.loadTexts: tfAlarmTCModule.setContactInfo('support@tail-f.com')
if mibBuilder.loadTexts: tfAlarmTCModule.setDescription('Textual conventions for alarms from Tail-f.')
class TfAlarmIndex(TextualConvention, Unsigned32):
    description = 'Index used in the alarm table. A row shall never change its index during the lifetime of the entry; for example renumbering entries is not allowed when entries are deleted. This integer is imaginary and has no meaning. The logical index in the alarm list is managed device, resource and alarm type.'
    status = 'current'
    displayHint = 'd'

class TfYANGResource(TextualConvention, OctetString):
    description = 'Identifies a resource using YANG instance identifers. A zero-length octet string means that the reference does not exist.'
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TfAlarmOperatorState(TextualConvention, Integer32):
    description = 'States for operator actions on alarms'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, 4, 5, 6)
    namedValues = NamedValues(("none", 1), ("ack", 2), ("investigation", 3), ("observation", 4), ("closed", 5), ("other", 6))

class TfUtf8String(TextualConvention, OctetString):
    description = 'To facilitate internationalization, this TC represents information taken from the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 character encoding scheme described in RFC 2044 [10]. For strings in 7-bit US-ASCII, there is no impact since the UTF-8 representation is identical to the US-ASCII encoding.'
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TfProbableCause(TextualConvention, Unsigned32):
    description = 'An integer value used for X.733 probable cause mapping. Since there are numerous conflicting probable cause enumeration mappings we leave this as a configurable integer.'
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("TAILF-ALARM-TC-MIB", TfAlarmIndex=TfAlarmIndex, TfAlarmOperatorState=TfAlarmOperatorState, TfUtf8String=TfUtf8String, tfAlarmTCModule=tfAlarmTCModule, TfYANGResource=TfYANGResource, TfProbableCause=TfProbableCause, PYSNMP_MODULE_ID=tfAlarmTCModule)
