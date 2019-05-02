#
# PySNMP MIB module FSM7326-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSM7326-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
fsm7326, = mibBuilder.importSymbols("FSM7326-REF-MIB", "fsm7326")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Integer32, MibIdentifier, Bits, Counter64, ObjectIdentity, iso, NotificationType, TimeTicks, Unsigned32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Integer32", "MibIdentifier", "Bits", "Counter64", "ObjectIdentity", "iso", "NotificationType", "TimeTicks", "Unsigned32", "Counter32", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fsm7326QOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3))
fsm7326QOS.setRevisions(('2003-11-10 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fsm7326QOS.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: fsm7326QOS.setLastUpdated('200311101200Z')
if mibBuilder.loadTexts: fsm7326QOS.setOrganization('Netgear')
if mibBuilder.loadTexts: fsm7326QOS.setContactInfo('')
if mibBuilder.loadTexts: fsm7326QOS.setDescription('')
mibBuilder.exportSymbols("FSM7326-QOS-MIB", PYSNMP_MODULE_ID=fsm7326QOS, fsm7326QOS=fsm7326QOS)
