#
# PySNMP MIB module DS8200v2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DS8200v2-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:54:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Bits, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Gauge32, IpAddress, ObjectIdentity, ModuleIdentity, enterprises, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Bits", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Gauge32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "enterprises", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
verilink = ModuleIdentity((1, 3, 6, 1, 4, 1, 321))
if mibBuilder.loadTexts: verilink.setLastUpdated('0011150000Z')
if mibBuilder.loadTexts: verilink.setOrganization('Verilink Corporation')
if mibBuilder.loadTexts: verilink.setContactInfo('Bob Ray bray@verilink.com 1-256-774-2380')
if mibBuilder.loadTexts: verilink.setDescription('DS8200v2 TC MIB.')
hbu = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100))
mibBuilder.exportSymbols("DS8200v2-TC-MIB", hbu=hbu, PYSNMP_MODULE_ID=verilink, verilink=verilink)
