#
# PySNMP MIB module DLINK-3100-DELETEIMG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-DELETEIMG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ObjectIdentity, Counter32, IpAddress, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Unsigned32, ModuleIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter32", "IpAddress", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Unsigned32", "ModuleIdentity", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DELETEIMGName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("image1", 1), ("image2", 2))

rlDeleteImg = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142))
rlDeleteImg.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlDeleteImg.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlDeleteImg.setOrganization('Dlink, Inc.')
rlDeleteImgTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1), )
if mibBuilder.loadTexts: rlDeleteImgTable.setStatus('current')
rlDeleteImgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1), ).setIndexNames((0, "DLINK-3100-DELETEIMG-MIB", "rlDeleteImgKey"))
if mibBuilder.loadTexts: rlDeleteImgEntry.setStatus('current')
rlDeleteImgKey = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: rlDeleteImgKey.setStatus('current')
rlDeleteImgUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteImgUnit.setStatus('current')
rlDeleteImgName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 3), DELETEIMGName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteImgName.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-DELETEIMG-MIB", rlDeleteImgKey=rlDeleteImgKey, rlDeleteImg=rlDeleteImg, rlDeleteImgTable=rlDeleteImgTable, DELETEIMGName=DELETEIMGName, PYSNMP_MODULE_ID=rlDeleteImg, rlDeleteImgUnit=rlDeleteImgUnit, rlDeleteImgEntry=rlDeleteImgEntry, rlDeleteImgName=rlDeleteImgName)
