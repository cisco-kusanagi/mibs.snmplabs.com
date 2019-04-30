#
# PySNMP MIB module ADTX-SMI-S2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTX-SMI-S2
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Unsigned32, TimeTicks, Integer32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, Gauge32, Counter32, iso, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Unsigned32", "TimeTicks", "Integer32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "Gauge32", "Counter32", "iso", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adtx = ModuleIdentity((1, 3, 6, 1, 4, 1, 2653))
adtx.setRevisions(('2003-01-22 00:00',))
if mibBuilder.loadTexts: adtx.setLastUpdated('200304220000Z')
if mibBuilder.loadTexts: adtx.setOrganization('ADTX (Advanced Technology and Systems Co., Ltd.)')
adtxReg = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 1))
adtxGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 2))
adtxProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 3))
adtxExpr = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 4))
avc = MibIdentifier((1, 3, 6, 1, 4, 1, 2653, 3, 1))
mibBuilder.exportSymbols("ADTX-SMI-S2", adtxExpr=adtxExpr, adtxGeneric=adtxGeneric, adtxReg=adtxReg, adtxProducts=adtxProducts, adtx=adtx, avc=avc, PYSNMP_MODULE_ID=adtx)
