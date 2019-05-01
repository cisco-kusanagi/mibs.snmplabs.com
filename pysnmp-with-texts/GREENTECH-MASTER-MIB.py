#
# PySNMP MIB module GREENTECH-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GREENTECH-MASTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:18:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Unsigned32, Counter64, NotificationType, Gauge32, ModuleIdentity, iso, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "iso", "Bits", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
greentech = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464))
greentech.setRevisions(('1900-08-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: greentech.setRevisionsDescriptions(('Initial MIB creation.',))
if mibBuilder.loadTexts: greentech.setLastUpdated('0008290000Z')
if mibBuilder.loadTexts: greentech.setOrganization('Greentech')
if mibBuilder.loadTexts: greentech.setContactInfo('Adam Armstrong E-mail: adama@memetic.org')
if mibBuilder.loadTexts: greentech.setDescription('Greentech Master MIB OID defines and documentation. Unofficial version for Observium use.')
dataCom = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1))
gbn = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 3))
gbnPlatform = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1))
gbnDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2))
gbnService = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 3))
gbnL2 = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4))
gbnL3 = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 5))
gbnLS = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 6))
gbnServiceAAA = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 1))
rmonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2))
mibBuilder.exportSymbols("GREENTECH-MASTER-MIB", PYSNMP_MODULE_ID=greentech, rmonMib=rmonMib, gbnDevice=gbnDevice, dataCom=dataCom, switch=switch, greentech=greentech, gbnService=gbnService, gbnLS=gbnLS, gbnServiceAAA=gbnServiceAAA, gbnPlatform=gbnPlatform, gbnL2=gbnL2, gbn=gbn, gbnL3=gbnL3)
