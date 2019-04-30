#
# PySNMP MIB module CISCO-NHRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NHRP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
nhrpCacheNbmaSubaddr, nhrpServerNbmaAddr, nhrpClientNhsNbmaAddrType, nhrpServerNbmaAddrType, nhrpServerInternetworkAddrType, nhrpCacheNbmaAddrType, nhrpServerNhcInternetworkAddr, nhrpServerNhcPrefixLength, nhrpClientNhsInternetworkAddr, nhrpClientNhsNbmaAddr, nhrpServerNbmaSubaddr, nhrpClientIndex, nhrpServerCacheUniqueness, nhrpCacheNextHopInternetworkAddr, nhrpClientNbmaAddr, nhrpClientInternetworkAddr, nhrpServerNhcNbmaAddr, nhrpServerNhcInUse, nhrpServerNhcNbmaAddrType, nhrpClientNhsInternetworkAddrType, nhrpClientInternetworkAddrType, nhrpClientStatEntry, nhrpCacheNbmaAddr, nhrpClientHoldTime, nhrpCacheType, nhrpServerNhcNbmaSubaddr, nhrpServerIndex, nhrpClientNbmaAddrType, nhrpClientNhsNbmaSubaddr, nhrpClientNhsInUse, nhrpClientNbmaSubaddr, nhrpClientRegUniqueness, nhrpServerInternetworkAddr, nhrpServerStatEntry, nhrpServerNhcInternetworkAddrType = mibBuilder.importSymbols("NHRP-MIB", "nhrpCacheNbmaSubaddr", "nhrpServerNbmaAddr", "nhrpClientNhsNbmaAddrType", "nhrpServerNbmaAddrType", "nhrpServerInternetworkAddrType", "nhrpCacheNbmaAddrType", "nhrpServerNhcInternetworkAddr", "nhrpServerNhcPrefixLength", "nhrpClientNhsInternetworkAddr", "nhrpClientNhsNbmaAddr", "nhrpServerNbmaSubaddr", "nhrpClientIndex", "nhrpServerCacheUniqueness", "nhrpCacheNextHopInternetworkAddr", "nhrpClientNbmaAddr", "nhrpClientInternetworkAddr", "nhrpServerNhcNbmaAddr", "nhrpServerNhcInUse", "nhrpServerNhcNbmaAddrType", "nhrpClientNhsInternetworkAddrType", "nhrpClientInternetworkAddrType", "nhrpClientStatEntry", "nhrpCacheNbmaAddr", "nhrpClientHoldTime", "nhrpCacheType", "nhrpServerNhcNbmaSubaddr", "nhrpServerIndex", "nhrpClientNbmaAddrType", "nhrpClientNhsNbmaSubaddr", "nhrpClientNhsInUse", "nhrpClientNbmaSubaddr", "nhrpClientRegUniqueness", "nhrpServerInternetworkAddr", "nhrpServerStatEntry", "nhrpServerNhcInternetworkAddrType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, Counter32, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNhrpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 680))
ciscoNhrpExtMIB.setRevisions(('2008-11-21 00:00',))
if mibBuilder.loadTexts: ciscoNhrpExtMIB.setLastUpdated('200811210000Z')
if mibBuilder.loadTexts: ciscoNhrpExtMIB.setOrganization('Cisco Systems, Inc.')
class CiscoNhrpErrorCode(TextualConvention, Integer32):
    reference = 'Sec.5.2.2, 5.2.4 and 5.2.7 of NHRP specification(RFC 2332) (April 1998)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 256))
    namedValues = NamedValues(("unrecogExtension", 1), ("loopDetected", 3), ("adminProhibited", 4), ("insufficientResources", 5), ("addressUnreachable", 6), ("protocolError", 7), ("sduSizeExceeded", 8), ("invalidExtension", 9), ("invalidResReply", 10), ("authFailure", 11), ("noAddressBinding", 12), ("bindingNotUnique", 13), ("uniqueInternetworkAddrRegd", 14), ("hopCountExceeded", 15), ("other", 256))

class CiscoNextHopDownReasonCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("administrative", 1), ("registrationFailure", 2), ("resolutionFailure", 3), ("purgeReceived", 4), ("normalExpiry", 5), ("external", 6), ("other", 7))

cneNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 0))
cneObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1))
cneConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 2))
cneGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1))
cneClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2))
cneServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3))
cneNotificationControlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 4))
cneNextHopDownReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1, 1), CiscoNextHopDownReasonCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cneNextHopDownReason.setStatus('current')
cneNHRPException = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1, 2), CiscoNhrpErrorCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cneNHRPException.setStatus('current')
cneClientStatExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1), )
if mibBuilder.loadTexts: cneClientStatExtTable.setStatus('current')
cneClientStatExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1, 1), )
nhrpClientStatEntry.registerAugmentions(("CISCO-NHRP-EXT-MIB", "cneClientStatExtEntry"))
cneClientStatExtEntry.setIndexNames(*nhrpClientStatEntry.getIndexNames())
if mibBuilder.loadTexts: cneClientStatExtEntry.setStatus('current')
cneClientStatRedirectRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cneClientStatRedirectRx.setStatus('current')
cneServerStatExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1), )
if mibBuilder.loadTexts: cneServerStatExtTable.setStatus('current')
cneServerStatExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1, 1), )
nhrpServerStatEntry.registerAugmentions(("CISCO-NHRP-EXT-MIB", "cneServerStatExtEntry"))
cneServerStatExtEntry.setIndexNames(*nhrpServerStatEntry.getIndexNames())
if mibBuilder.loadTexts: cneServerStatExtEntry.setStatus('current')
cneServerStatRedirectTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cneServerStatRedirectTx.setStatus('current')
cneNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 4, 1), Bits().clone(namedValues=NamedValues(("nextHopRegServerUp", 0), ("nextHopRegServerDown", 1), ("nextHopRegClientUp", 2), ("nextHopRegClientDown", 3), ("nextHopPeerUp", 4), ("nextHopPeerDown", 5), ("rateLimitExceeded", 6))).clone(namedValues=NamedValues(("nextHopRegServerUp", 0), ("nextHopRegServerDown", 1), ("nextHopRegClientUp", 2), ("nextHopRegClientDown", 3), ("rateLimitExceeded", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cneNotifEnable.setStatus('current')
cneNotifNextHopRegServerUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 1)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddrType"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaAddrType"), ("NHRP-MIB", "nhrpClientNhsNbmaAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaSubaddr"), ("NHRP-MIB", "nhrpClientHoldTime"), ("NHRP-MIB", "nhrpClientRegUniqueness"), ("NHRP-MIB", "nhrpClientNhsInUse"))
if mibBuilder.loadTexts: cneNotifNextHopRegServerUp.setStatus('current')
cneNotifNextHopRegServerDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 2)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddrType"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaAddrType"), ("NHRP-MIB", "nhrpClientNhsNbmaAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaSubaddr"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"), ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
if mibBuilder.loadTexts: cneNotifNextHopRegServerDown.setStatus('current')
cneNotifNextHopRegClientUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 3)).setObjects(("NHRP-MIB", "nhrpServerInternetworkAddrType"), ("NHRP-MIB", "nhrpServerInternetworkAddr"), ("NHRP-MIB", "nhrpServerNbmaAddrType"), ("NHRP-MIB", "nhrpServerNbmaAddr"), ("NHRP-MIB", "nhrpServerNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddrType"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaAddrType"), ("NHRP-MIB", "nhrpServerNhcNbmaAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcPrefixLength"), ("NHRP-MIB", "nhrpServerNhcInUse"), ("NHRP-MIB", "nhrpServerCacheUniqueness"))
if mibBuilder.loadTexts: cneNotifNextHopRegClientUp.setStatus('current')
cneNotifNextHopRegClientDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 4)).setObjects(("NHRP-MIB", "nhrpServerInternetworkAddrType"), ("NHRP-MIB", "nhrpServerInternetworkAddr"), ("NHRP-MIB", "nhrpServerNbmaAddrType"), ("NHRP-MIB", "nhrpServerNbmaAddr"), ("NHRP-MIB", "nhrpServerNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddrType"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaAddrType"), ("NHRP-MIB", "nhrpServerNhcNbmaAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcPrefixLength"), ("NHRP-MIB", "nhrpServerCacheUniqueness"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"), ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
if mibBuilder.loadTexts: cneNotifNextHopRegClientDown.setStatus('current')
cneNotifNextHopPeerUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 5)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpCacheNextHopInternetworkAddr"), ("NHRP-MIB", "nhrpCacheNbmaAddrType"), ("NHRP-MIB", "nhrpCacheNbmaAddr"), ("NHRP-MIB", "nhrpCacheNbmaSubaddr"), ("NHRP-MIB", "nhrpCacheType"))
if mibBuilder.loadTexts: cneNotifNextHopPeerUp.setStatus('current')
cneNotifNextHopPeerDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 6)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpCacheNextHopInternetworkAddr"), ("NHRP-MIB", "nhrpCacheNbmaAddrType"), ("NHRP-MIB", "nhrpCacheNbmaAddr"), ("NHRP-MIB", "nhrpCacheNbmaSubaddr"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"), ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
if mibBuilder.loadTexts: cneNotifNextHopPeerDown.setStatus('current')
cneNotifRateLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 7)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: cneNotifRateLimitExceeded.setStatus('current')
cneCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 1))
cneGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2))
cneCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 1, 1)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotificationControlGroup"), ("CISCO-NHRP-EXT-MIB", "cneGeneralNotificationGroup"), ("CISCO-NHRP-EXT-MIB", "cneGeneralGroup"), ("CISCO-NHRP-EXT-MIB", "cneClientNotificationGroup"), ("CISCO-NHRP-EXT-MIB", "cneServerNotificationGroup"), ("CISCO-NHRP-EXT-MIB", "cneClientGroup"), ("CISCO-NHRP-EXT-MIB", "cneServerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneCompliance = cneCompliance.setStatus('current')
cneGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 1)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNHRPException"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneGeneralGroup = cneGeneralGroup.setStatus('current')
cneClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 2)).setObjects(("CISCO-NHRP-EXT-MIB", "cneClientStatRedirectRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneClientGroup = cneClientGroup.setStatus('current')
cneServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 3)).setObjects(("CISCO-NHRP-EXT-MIB", "cneServerStatRedirectTx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneServerGroup = cneServerGroup.setStatus('current')
cneNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 4)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneNotificationControlGroup = cneNotificationControlGroup.setStatus('current')
cneGeneralNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 5)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifRateLimitExceeded"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopPeerUp"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopPeerDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneGeneralNotificationGroup = cneGeneralNotificationGroup.setStatus('current')
cneClientNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 6)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegServerUp"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegServerDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneClientNotificationGroup = cneClientNotificationGroup.setStatus('current')
cneServerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 7)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegClientUp"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegClientDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneServerNotificationGroup = cneServerNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NHRP-EXT-MIB", cneClientObjects=cneClientObjects, cneNotifRateLimitExceeded=cneNotifRateLimitExceeded, cneConform=cneConform, cneCompliances=cneCompliances, cneGroups=cneGroups, cneNotifNextHopPeerDown=cneNotifNextHopPeerDown, cneCompliance=cneCompliance, cneClientStatExtTable=cneClientStatExtTable, cneNotifNextHopRegClientUp=cneNotifNextHopRegClientUp, cneNHRPException=cneNHRPException, cneServerStatExtEntry=cneServerStatExtEntry, cneNotifEnable=cneNotifEnable, CiscoNhrpErrorCode=CiscoNhrpErrorCode, cneNotificationControlGroup=cneNotificationControlGroup, cneServerStatRedirectTx=cneServerStatRedirectTx, cneNotifNextHopRegServerUp=cneNotifNextHopRegServerUp, cneObjects=cneObjects, cneGeneralNotificationGroup=cneGeneralNotificationGroup, cneServerGroup=cneServerGroup, cneNotifNextHopRegClientDown=cneNotifNextHopRegClientDown, cneNotifNextHopRegServerDown=cneNotifNextHopRegServerDown, cneClientGroup=cneClientGroup, cneGeneralGroup=cneGeneralGroup, cneClientNotificationGroup=cneClientNotificationGroup, cneServerNotificationGroup=cneServerNotificationGroup, cneGeneralObjects=cneGeneralObjects, cneNotifs=cneNotifs, cneServerStatExtTable=cneServerStatExtTable, cneNotifNextHopPeerUp=cneNotifNextHopPeerUp, cneServerObjects=cneServerObjects, cneNotificationControlObjects=cneNotificationControlObjects, CiscoNextHopDownReasonCode=CiscoNextHopDownReasonCode, ciscoNhrpExtMIB=ciscoNhrpExtMIB, cneClientStatRedirectRx=cneClientStatRedirectRx, cneNextHopDownReason=cneNextHopDownReason, cneClientStatExtEntry=cneClientStatExtEntry, PYSNMP_MODULE_ID=ciscoNhrpExtMIB)
