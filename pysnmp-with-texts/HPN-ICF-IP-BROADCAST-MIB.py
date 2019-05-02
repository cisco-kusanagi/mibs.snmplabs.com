#
# PySNMP MIB module HPN-ICF-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-IP-BROADCAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, Counter32, TimeTicks, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, MibIdentifier, Counter64, iso, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Counter32", "TimeTicks", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "MibIdentifier", "Counter64", "iso", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33))
hpnicfIpBroadcast.setRevisions(('2004-12-13 19:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfIpBroadcast.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: hpnicfIpBroadcast.setOrganization('')
if mibBuilder.loadTexts: hpnicfIpBroadcast.setContactInfo('')
if mibBuilder.loadTexts: hpnicfIpBroadcast.setDescription('This MIB is objects used to describe IP broadcast features or functions. Some objects in this may be used only for some specific products, so users should refer to the related documents to acquire more detail information. ')
hpnicfIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1))
hpnicfIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpBdstForwardBroadcast.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpBdstForwardBroadcast.setDescription('This object indicates whether a device forwards direct broadcast datagrams or not. More details of this object, please refers to RFC2644. ')
hpnicfIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpReceiveBroadcast.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpReceiveBroadcast.setDescription('This objects indicates whether a device receives direct broadcast datagrams or not. More details of this object, please refers to RFC2644. ')
hpnicfIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 2))
hpnicfIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3))
hpnicfIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3, 0))
mibBuilder.exportSymbols("HPN-ICF-IP-BROADCAST-MIB", hpnicfIpBdstForwardBroadcast=hpnicfIpBdstForwardBroadcast, hpnicfIpBroadcast=hpnicfIpBroadcast, hpnicfIpBdstTrapPrex=hpnicfIpBdstTrapPrex, hpnicfIpBdstScalarGroup=hpnicfIpBdstScalarGroup, hpnicfIpBdstGroup=hpnicfIpBdstGroup, hpnicfIpReceiveBroadcast=hpnicfIpReceiveBroadcast, hpnicfIpBdstTrap=hpnicfIpBdstTrap, PYSNMP_MODULE_ID=hpnicfIpBroadcast)
