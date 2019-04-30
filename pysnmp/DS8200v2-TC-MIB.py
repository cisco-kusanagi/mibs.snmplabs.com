#
# PySNMP MIB module DS8200v2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DS8200v2-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:39:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, Counter32, ObjectIdentity, ModuleIdentity, TimeTicks, Counter64, enterprises, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Counter32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter64", "enterprises", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
verilink = ModuleIdentity((1, 3, 6, 1, 4, 1, 321))
if mibBuilder.loadTexts: verilink.setLastUpdated('0011150000Z')
if mibBuilder.loadTexts: verilink.setOrganization('Verilink Corporation')
hbu = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100))
mibBuilder.exportSymbols("DS8200v2-TC-MIB", PYSNMP_MODULE_ID=verilink, hbu=hbu, verilink=verilink)
