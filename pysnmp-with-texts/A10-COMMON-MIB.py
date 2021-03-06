#
# PySNMP MIB module A10-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A10-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:03:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, IpAddress, MibIdentifier, enterprises, Gauge32, iso, ObjectIdentity, NotificationType, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "IpAddress", "MibIdentifier", "enterprises", "Gauge32", "iso", "ObjectIdentity", "NotificationType", "Counter64", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a10 = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610))
if mibBuilder.loadTexts: a10.setLastUpdated('200611071327Z')
if mibBuilder.loadTexts: a10.setOrganization('A10 Networks, Inc.')
if mibBuilder.loadTexts: a10.setContactInfo('Address: A10 Networks, Inc. 2309 Bering Drive San Jose, CA 95131 Phone: +1-888-822-7210 (USA/Canada) +1-408-325-8676 (International) E-mail: support@A10Networks.com')
if mibBuilder.loadTexts: a10.setDescription('This file defines the private enterprise MIB of A10 Networks, Inc.')
a10Products = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1))
if mibBuilder.loadTexts: a10Products.setStatus('current')
if mibBuilder.loadTexts: a10Products.setDescription('a10Products is the root OBJECT IDENTIFIER from which sysObjectID values are assigned.')
a10Mgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 2))
if mibBuilder.loadTexts: a10Mgmt.setStatus('current')
if mibBuilder.loadTexts: a10Mgmt.setDescription('root OID of A10 product management MIBs')
a10IDsentrie = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 1))
if mibBuilder.loadTexts: a10IDsentrie.setStatus('current')
if mibBuilder.loadTexts: a10IDsentrie.setDescription('OID assigned to the IDsentrie family appliances')
a10IDsentrie1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 1, 1))
if mibBuilder.loadTexts: a10IDsentrie1000.setStatus('current')
if mibBuilder.loadTexts: a10IDsentrie1000.setDescription('OID assigned to the model, IDsentrie 1000 appliance')
a10StealthWatch = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 1, 2))
if mibBuilder.loadTexts: a10StealthWatch.setStatus('current')
if mibBuilder.loadTexts: a10StealthWatch.setDescription('OID assigned to the StealthWatch IDentity 1000 appliance')
a10RetiEntity1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 1, 3))
if mibBuilder.loadTexts: a10RetiEntity1000.setStatus('current')
if mibBuilder.loadTexts: a10RetiEntity1000.setDescription('OID assigned to the RetiEntity 1000 appliance')
a10EX = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 2))
if mibBuilder.loadTexts: a10EX.setStatus('current')
if mibBuilder.loadTexts: a10EX.setDescription('OID assigned to the Edge accelerator family appliances')
a10EX2100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 2, 1))
if mibBuilder.loadTexts: a10EX2100.setStatus('current')
if mibBuilder.loadTexts: a10EX2100.setDescription('OID assigned to the model, Edge accelerator EX2100, appliance')
a10EX2180 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 2, 2))
if mibBuilder.loadTexts: a10EX2180.setStatus('current')
if mibBuilder.loadTexts: a10EX2180.setDescription('OID assigned to the model, Edge accelerator EX2180, appliance')
a10EX2200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 2, 3))
if mibBuilder.loadTexts: a10EX2200.setStatus('current')
if mibBuilder.loadTexts: a10EX2200.setDescription('OID assigned to the model, Edge accelerator EX2200, appliance')
a10EX2280 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 2, 4))
if mibBuilder.loadTexts: a10EX2280.setStatus('current')
if mibBuilder.loadTexts: a10EX2280.setDescription('OID assigned to the model, Edge accelerator EX2280, appliance')
a10AX = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3))
if mibBuilder.loadTexts: a10AX.setStatus('current')
if mibBuilder.loadTexts: a10AX.setDescription('OID assigned to the advanced traffic manager product family')
a10AX2100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 1))
if mibBuilder.loadTexts: a10AX2100.setStatus('current')
if mibBuilder.loadTexts: a10AX2100.setDescription('OID assigned to the model, AX2100 Advanced Traffic Manager')
a10AX3100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 2))
if mibBuilder.loadTexts: a10AX3100.setStatus('current')
if mibBuilder.loadTexts: a10AX3100.setDescription('OID assigned to the model, AX3100 Advanced Traffic Manager')
a10AX3200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 3))
if mibBuilder.loadTexts: a10AX3200.setStatus('current')
if mibBuilder.loadTexts: a10AX3200.setDescription('OID assigned to the model, AX3200 Advanced Traffic Manager')
a10AX2200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 4))
if mibBuilder.loadTexts: a10AX2200.setStatus('current')
if mibBuilder.loadTexts: a10AX2200.setDescription('OID assigned to the model, AX2200 Advanced Traffic Manager')
a10AX2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 5))
if mibBuilder.loadTexts: a10AX2000.setStatus('current')
if mibBuilder.loadTexts: a10AX2000.setDescription('OID assigned to the model, AX2000 Advanced Traffic Manager')
a10AX1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 6))
if mibBuilder.loadTexts: a10AX1000.setStatus('current')
if mibBuilder.loadTexts: a10AX1000.setDescription('OID assigned to the model, AX1000 Advanced Traffic Manager')
a10AX5200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 7))
if mibBuilder.loadTexts: a10AX5200.setStatus('current')
if mibBuilder.loadTexts: a10AX5200.setDescription('OID assigned to the model, AX5200 Advanced Traffic Manager')
a10AX2500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 8))
if mibBuilder.loadTexts: a10AX2500.setStatus('current')
if mibBuilder.loadTexts: a10AX2500.setDescription('OID assigned to the model, AX2500 Advanced Traffic Manager')
a10AX2600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 9))
if mibBuilder.loadTexts: a10AX2600.setStatus('current')
if mibBuilder.loadTexts: a10AX2600.setDescription('OID assigned to the model, AX2600 Advanced Traffic Manager')
a10AX3000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 10))
if mibBuilder.loadTexts: a10AX3000.setStatus('current')
if mibBuilder.loadTexts: a10AX3000.setDescription('OID assigned to the model, AX3000 Advanced Traffic Manager')
a10HitachiBladeServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 11))
if mibBuilder.loadTexts: a10HitachiBladeServer.setStatus('current')
if mibBuilder.loadTexts: a10HitachiBladeServer.setDescription('OID assigned to the model, Hitachi Blade Server Advanced Traffic Manager')
a10AX5100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 22610, 1, 3, 12))
if mibBuilder.loadTexts: a10AX5100.setStatus('current')
if mibBuilder.loadTexts: a10AX5100.setDescription('OID assigned to the model, AX5100 Advanced Traffic Manager')
mibBuilder.exportSymbols("A10-COMMON-MIB", a10EX2280=a10EX2280, a10AX2100=a10AX2100, a10AX2500=a10AX2500, a10StealthWatch=a10StealthWatch, a10RetiEntity1000=a10RetiEntity1000, a10AX3000=a10AX3000, a10Mgmt=a10Mgmt, a10HitachiBladeServer=a10HitachiBladeServer, PYSNMP_MODULE_ID=a10, a10EX2180=a10EX2180, a10AX5200=a10AX5200, a10AX1000=a10AX1000, a10Products=a10Products, a10EX2200=a10EX2200, a10EX2100=a10EX2100, a10IDsentrie1000=a10IDsentrie1000, a10=a10, a10AX3100=a10AX3100, a10AX5100=a10AX5100, a10AX3200=a10AX3200, a10AX2200=a10AX2200, a10AX2000=a10AX2000, a10EX=a10EX, a10AX=a10AX, a10AX2600=a10AX2600, a10IDsentrie=a10IDsentrie)
