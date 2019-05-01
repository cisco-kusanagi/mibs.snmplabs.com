#
# PySNMP MIB module HH3C-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-IP-BROADCAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Counter32, NotificationType, Counter64, Unsigned32, Integer32, IpAddress, MibIdentifier, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter32", "NotificationType", "Counter64", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 33))
hh3cIpBroadcast.setRevisions(('2004-12-13 19:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cIpBroadcast.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: hh3cIpBroadcast.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cIpBroadcast.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cIpBroadcast.setDescription('This MIB is objects used to describe IP broadcast features or functions. Some objects in this may be used only for some specific products, so users should refer to the related documents to acquire more detail information. ')
hh3cIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 1))
hh3cIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpBdstForwardBroadcast.setStatus('current')
if mibBuilder.loadTexts: hh3cIpBdstForwardBroadcast.setDescription('This object indicates whether a device forwards direct broadcast datagrams or not. More details of this object, please refers to RFC2644. ')
hh3cIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpReceiveBroadcast.setStatus('current')
if mibBuilder.loadTexts: hh3cIpReceiveBroadcast.setDescription('This objects indicates whether a device receives direct broadcast datagrams or not. More details of this object, please refers to RFC2644. ')
hh3cIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 2))
hh3cIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 3))
hh3cIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 3, 0))
mibBuilder.exportSymbols("HH3C-IP-BROADCAST-MIB", PYSNMP_MODULE_ID=hh3cIpBroadcast, hh3cIpBroadcast=hh3cIpBroadcast, hh3cIpBdstScalarGroup=hh3cIpBdstScalarGroup, hh3cIpBdstTrapPrex=hh3cIpBdstTrapPrex, hh3cIpBdstTrap=hh3cIpBdstTrap, hh3cIpReceiveBroadcast=hh3cIpReceiveBroadcast, hh3cIpBdstForwardBroadcast=hh3cIpBdstForwardBroadcast, hh3cIpBdstGroup=hh3cIpBdstGroup)
