#
# PySNMP MIB module GSM7312-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7312-REF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, iso, Counter64, MibIdentifier, TimeTicks, Gauge32, Counter32, NotificationType, IpAddress, Unsigned32, Bits, ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "iso", "Counter64", "MibIdentifier", "TimeTicks", "Gauge32", "Counter32", "NotificationType", "IpAddress", "Unsigned32", "Bits", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
snmpManagedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1))
gsm7312 = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 6))
gsm7312.setRevisions(('2003-05-06 12:00',))
if mibBuilder.loadTexts: gsm7312.setLastUpdated('200305061200Z')
if mibBuilder.loadTexts: gsm7312.setOrganization('Netgear')
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("GSM7312-REF-MIB", netgear=netgear, AgentPortMask=AgentPortMask, PYSNMP_MODULE_ID=gsm7312, snmpManagedSwitch=snmpManagedSwitch, gsm7312=gsm7312)
