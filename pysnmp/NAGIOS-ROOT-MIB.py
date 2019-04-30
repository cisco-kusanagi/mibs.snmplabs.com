#
# PySNMP MIB module NAGIOS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NAGIOS-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Counter32, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, NotificationType, Integer32, Counter64, enterprises, IpAddress, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter32", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "Integer32", "Counter64", "enterprises", "IpAddress", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nagios = ModuleIdentity((1, 3, 6, 1, 4, 1, 20006))
nagios.setRevisions(('2005-03-09 00:00', '2005-01-20 00:00',))
if mibBuilder.loadTexts: nagios.setLastUpdated('200503090000Z')
if mibBuilder.loadTexts: nagios.setOrganization('Nagios')
class NotifyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("problem", 0), ("recovery", 1), ("acknowledgement", 2), ("flappingstart", 3), ("flappingstop", 4))

class HostStateID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3))
    namedValues = NamedValues(("up", 0), ("down", 1), ("unreachable", 3))

class HostStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("hard", 0), ("soft", 1))

class ServiceStateID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("warning", 1), ("critical", 2), ("unknown", 3))

mibBuilder.exportSymbols("NAGIOS-ROOT-MIB", PYSNMP_MODULE_ID=nagios, HostStateID=HostStateID, ServiceStateID=ServiceStateID, nagios=nagios, HostStateType=HostStateType, NotifyType=NotifyType)
