#
# PySNMP MIB module HH3C-ATM-DXI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-ATM-DXI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Counter32, IpAddress, Unsigned32, TimeTicks, ObjectIdentity, Gauge32, Integer32, ModuleIdentity, Counter64, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "IpAddress", "Unsigned32", "TimeTicks", "ObjectIdentity", "Gauge32", "Integer32", "ModuleIdentity", "Counter64", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hh3cAtmDxi = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 49))
hh3cAtmDxi.setRevisions(('2005-04-14 15:18',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cAtmDxi.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cAtmDxi.setLastUpdated('200504141518Z')
if mibBuilder.loadTexts: hh3cAtmDxi.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cAtmDxi.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cAtmDxi.setDescription('This MIB contains objects to manage configuration of ATM-DXI. There are no constraints on this MIB.')
hh3cAtmDxiScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 49, 1))
hh3cAtmDxiConfMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 49, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cAtmDxiConfMode.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiConfMode.setDescription('This node identifies the ATM-DXI mode being used at the ATM-DXI port.')
hh3cAtmDxiIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2))
hh3cAtmDxiPvcTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1), )
if mibBuilder.loadTexts: hh3cAtmDxiPvcTable.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcTable.setDescription('This table describes information of PVC in ATM-DXI interface.')
hh3cAtmDxiPvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcVpi"), (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcVci"))
if mibBuilder.loadTexts: hh3cAtmDxiPvcEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcEntry.setDescription('The entry of hh3cAtmDxiPvcTable.')
hh3cAtmDxiPvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: hh3cAtmDxiPvcVpi.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcVpi.setDescription("The value of VPI. It can't be 0 if hh3cAtmDxiPvcVci is 0.")
hh3cAtmDxiPvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: hh3cAtmDxiPvcVci.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcVci.setDescription("The value of VCI. It can't be 0 if hh3cAtmDxiPvcVpi is 0.")
hh3cAtmDxiPvcDFA = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAtmDxiPvcDFA.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcDFA.setDescription('The index of PVC. It is equal with vci and VPI. And this node value is correlate with hh3cAtmDxiPvcVpi and hh3cAtmDxiPvcVci. ')
hh3cAtmDxiPvcEncType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("snap", 1), ("nlpid", 2), ("mux", 3))).clone('snap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAtmDxiPvcEncType.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcEncType.setDescription('Encapsulation type of the frame.')
hh3cAtmDxiPvcMapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAtmDxiPvcMapCount.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcMapCount.setDescription('The number of map. One map can only associate with one PVC, but one PVC can associate with 32 maps. This node is the map count which one PVC associated with.')
hh3cAtmDxiPvcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAtmDxiPvcRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiPvcRowStatus.setDescription("Only support 'destroy' 'createAndGo' and 'active'.")
hh3cAtmDxiMapTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2), )
if mibBuilder.loadTexts: hh3cAtmDxiMapTable.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapTable.setDescription('This table describes PVC map information.')
hh3cAtmDxiMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPeerIpType"), (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPeerIp"), (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPvcVpi"), (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPvcVci"), (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapType"))
if mibBuilder.loadTexts: hh3cAtmDxiMapEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapEntry.setDescription('The entry of hh3cAtmDxiMapTable.')
hh3cAtmDxiMapPeerIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cAtmDxiMapPeerIpType.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapPeerIpType.setDescription('The type of ip address: IPv4 or IPv6.')
hh3cAtmDxiMapPeerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: hh3cAtmDxiMapPeerIp.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapPeerIp.setDescription('The peer ip address. This ip address is the peer ip address which the frame will arrive.')
hh3cAtmDxiMapPvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: hh3cAtmDxiMapPvcVpi.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapPvcVpi.setDescription("The VPI of PVC. It can't be 0 if hh3cAtmDxiMapPvcVci is 0.")
hh3cAtmDxiMapPvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: hh3cAtmDxiMapPvcVci.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapPvcVci.setDescription("The VCI of PVC. It can't be 0 if hh3cAtmDxiMapPvcVpi is 0.")
hh3cAtmDxiMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("address", 1), ("inarp", 2), ("default", 3))))
if mibBuilder.loadTexts: hh3cAtmDxiMapType.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapType.setDescription('Pvc map type.')
hh3cAtmDxiMapInarpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 10), )).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAtmDxiMapInarpTime.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapInarpTime.setDescription("The interval time of inarp request. This node describes the interval time inarp request frame sent. If the hh3cAtmDxiMapType isn't inarp, this value is 0. Its unit is minute.")
hh3cAtmDxiMapBroEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAtmDxiMapBroEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapBroEnable.setDescription('Whether ATM-DXI map enable broadcast or not.')
hh3cAtmDxiMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAtmDxiMapRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiMapRowStatus.setDescription("Only support 'destroy', 'createAndGo' and 'active'.")
hh3cAtmDxiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 49, 3))
hh3cAtmDxiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 1))
hh3cAtmDxiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 1, 1)).setObjects(("HH3C-ATM-DXI-MIB", "hh3cPVCMAPGroup"), ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cAtmDxiCompliance = hh3cAtmDxiCompliance.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiCompliance.setDescription('The compliance statement.')
hh3cAtmDxiGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 2))
hh3cPVCMAPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 2, 1)).setObjects(("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcDFA"), ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcEncType"), ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcMapCount"), ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcRowStatus"), ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapBroEnable"), ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapInarpTime"), ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPVCMAPGroup = hh3cPVCMAPGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cPVCMAPGroup.setDescription('This group includes nodes which are associated with interface.')
hh3cAtmDxiGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 2, 2)).setObjects(("HH3C-ATM-DXI-MIB", "hh3cAtmDxiConfMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cAtmDxiGeneralGroup = hh3cAtmDxiGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cAtmDxiGeneralGroup.setDescription('This group includes the general nodes about ATM-DXI.')
mibBuilder.exportSymbols("HH3C-ATM-DXI-MIB", hh3cAtmDxiMapRowStatus=hh3cAtmDxiMapRowStatus, hh3cAtmDxiScalarGroup=hh3cAtmDxiScalarGroup, hh3cAtmDxiMapPeerIpType=hh3cAtmDxiMapPeerIpType, hh3cAtmDxiPvcVci=hh3cAtmDxiPvcVci, hh3cAtmDxiPvcRowStatus=hh3cAtmDxiPvcRowStatus, hh3cPVCMAPGroup=hh3cPVCMAPGroup, hh3cAtmDxiPvcVpi=hh3cAtmDxiPvcVpi, PYSNMP_MODULE_ID=hh3cAtmDxi, hh3cAtmDxiIfObjects=hh3cAtmDxiIfObjects, hh3cAtmDxiConfMode=hh3cAtmDxiConfMode, hh3cAtmDxiPvcTable=hh3cAtmDxiPvcTable, hh3cAtmDxiMapBroEnable=hh3cAtmDxiMapBroEnable, hh3cAtmDxiMapPeerIp=hh3cAtmDxiMapPeerIp, hh3cAtmDxiCompliance=hh3cAtmDxiCompliance, hh3cAtmDxiPvcEntry=hh3cAtmDxiPvcEntry, hh3cAtmDxiMapEntry=hh3cAtmDxiMapEntry, hh3cAtmDxiMapPvcVci=hh3cAtmDxiMapPvcVci, hh3cAtmDxiGeneralGroup=hh3cAtmDxiGeneralGroup, hh3cAtmDxiPvcMapCount=hh3cAtmDxiPvcMapCount, hh3cAtmDxiMapInarpTime=hh3cAtmDxiMapInarpTime, hh3cAtmDxiCompliances=hh3cAtmDxiCompliances, hh3cAtmDxiMapType=hh3cAtmDxiMapType, hh3cAtmDxiPvcEncType=hh3cAtmDxiPvcEncType, hh3cAtmDxiPvcDFA=hh3cAtmDxiPvcDFA, hh3cAtmDxi=hh3cAtmDxi, hh3cAtmDxiMapPvcVpi=hh3cAtmDxiMapPvcVpi, hh3cAtmDxiMapTable=hh3cAtmDxiMapTable, hh3cAtmDxiConformance=hh3cAtmDxiConformance, hh3cAtmDxiGroup=hh3cAtmDxiGroup)
