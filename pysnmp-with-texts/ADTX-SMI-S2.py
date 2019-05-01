#
# PySNMP MIB module ADTX-SMI-S2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTX-SMI-S2
# Produced by pysmi-0.3.4 at Wed May  1 11:15:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, enterprises, ModuleIdentity, Integer32, Gauge32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, IpAddress, Unsigned32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "enterprises", "ModuleIdentity", "Integer32", "Gauge32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "IpAddress", "Unsigned32", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adtx = ModuleIdentity((1, 3, 6, 1, 4, 1, 2653))
adtx.setRevisions(('2003-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adtx.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: adtx.setLastUpdated('200304220000Z')
if mibBuilder.loadTexts: adtx.setOrganization('ADTX (Advanced Technology and Systems Co., Ltd.)')
if mibBuilder.loadTexts: adtx.setContactInfo('Customer Service Officer Postal: Yokohama Business Park East Tower 9F 134 Goudo-cho, Hodogaya-ku, Yokohama-shi, Kanagawa-ken 240-0005 Japan Tel: +81-45-334-0040 E-mail: cso@adtx.com')
if mibBuilder.loadTexts: adtx.setDescription('The Structure of Management Information for the ADTX enterprise.')
adtxReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 1))
adtxGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 2))
adtxProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 3))
adtxExpr = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 4))
avc = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 3, 1))
mibBuilder.exportSymbols("ADTX-SMI-S2", adtxExpr=adtxExpr, adtxGeneric=adtxGeneric, adtxReg=adtxReg, adtxProducts=adtxProducts, avc=avc, PYSNMP_MODULE_ID=adtx, adtx=adtx)
