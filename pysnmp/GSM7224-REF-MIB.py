#
# PySNMP MIB module GSM7224-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7224-REF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ObjectIdentity, Unsigned32, TimeTicks, ModuleIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Bits, Counter32, Counter64, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Unsigned32", "TimeTicks", "ModuleIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Bits", "Counter32", "Counter64", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
snmpManagedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1))
gsm7224 = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 8))
gsm7224.setRevisions(('2003-05-06 12:00',))
if mibBuilder.loadTexts: gsm7224.setLastUpdated('200311101200Z')
if mibBuilder.loadTexts: gsm7224.setOrganization('Netgear')
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("GSM7224-REF-MIB", PYSNMP_MODULE_ID=gsm7224, AgentPortMask=AgentPortMask, gsm7224=gsm7224, netgear=netgear, snmpManagedSwitch=snmpManagedSwitch)
