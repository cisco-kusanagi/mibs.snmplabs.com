#
# PySNMP MIB module H3C-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-IP-BROADCAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Counter64, NotificationType, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, iso, TimeTicks, Integer32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "iso", "TimeTicks", "Integer32", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33))
h3cIpBroadcast.setRevisions(('2004-12-13 19:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cIpBroadcast.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: h3cIpBroadcast.setOrganization('Huawei 3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cIpBroadcast.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085 ')
if mibBuilder.loadTexts: h3cIpBroadcast.setDescription('This MIB is objects used to describe IP broadcast features or functions. Some objects in this may be used only for some specific products, so users should refer to the related documents to acquire more detail information. ')
h3cIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 1))
h3cIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpBdstForwardBroadcast.setStatus('current')
if mibBuilder.loadTexts: h3cIpBdstForwardBroadcast.setDescription('This object indicates whether a device forwards direct broadcast datagrams or not. More details of this object, please refers to RFC2644. ')
h3cIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpReceiveBroadcast.setStatus('current')
if mibBuilder.loadTexts: h3cIpReceiveBroadcast.setDescription('This objects indicates whether a device receives direct broadcast datagrams or not. More details of this object, please refers to RFC2644. ')
h3cIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 2))
h3cIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 3))
h3cIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 3, 0))
mibBuilder.exportSymbols("H3C-IP-BROADCAST-MIB", h3cIpBdstGroup=h3cIpBdstGroup, h3cIpBroadcast=h3cIpBroadcast, h3cIpBdstTrapPrex=h3cIpBdstTrapPrex, h3cIpBdstTrap=h3cIpBdstTrap, h3cIpBdstScalarGroup=h3cIpBdstScalarGroup, h3cIpReceiveBroadcast=h3cIpReceiveBroadcast, h3cIpBdstForwardBroadcast=h3cIpBdstForwardBroadcast, PYSNMP_MODULE_ID=h3cIpBroadcast)
