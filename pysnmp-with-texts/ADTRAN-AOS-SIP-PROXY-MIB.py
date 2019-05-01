#
# PySNMP MIB module ADTRAN-AOS-SIP-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOS-SIP-PROXY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:14:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSConformance, adGenAOSVoice = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSVoice")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, TimeTicks, Counter32, Integer32, NotificationType, iso, ObjectIdentity, Gauge32, IpAddress, ModuleIdentity, Bits, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Counter32", "Integer32", "NotificationType", "iso", "ObjectIdentity", "Gauge32", "IpAddress", "ModuleIdentity", "Bits", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSSipProxy = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 5))
adGenAOSSipProxy.setRevisions(('2013-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSSipProxy.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSSipProxy.setLastUpdated('201305160000Z')
if mibBuilder.loadTexts: adGenAOSSipProxy.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSSipProxy.setContactInfo('Technical Support Dept. Postal: ADTRAN, Inc. 901 Explorer Blvd. Huntsville, AL 35806 Tel: +1 800 726-8663 Fax: +1 256 963 6217 E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSSipProxy.setDescription('This MIB contains information regarding SIP Proxy.')
adSipProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5))
adSipProxyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0))
adProxyTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 1), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyTimestamp.setStatus('current')
if mibBuilder.loadTexts: adProxyTimestamp.setDescription('The time (seconds since epoch) that a Proxy event occurred and not necessarily the when the trap was sent.')
adProxyRolloverFromServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddressType.setStatus('current')
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddressType.setDescription('The address type of adProxyRolloverFromServerInetAddressType')
adProxyRolloverFromServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddress.setDescription('The IP address of previous active Proxy SIP Server')
adProxyRolloverToServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 4), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddressType.setStatus('current')
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddressType.setDescription('The address type of adProxyRolloverToServerInetAddressType')
adProxyRolloverToServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 5), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddress.setDescription('The IP address of new active Proxy SIP Server')
class AdProxyRolloverCauseTC(TextualConvention, Integer32):
    description = 'The transactionFailed(1) state indicates that rollover occurred because a SIP transaction failed. The pollFailed(2) state indicates that rollover occurred because OPTIONS poll to current server failed. The pollSucceeded(3) state indicates that rollback occurred because OPTIONS poll to failed server succeeded.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("transactionFailed", 1), ("pollFailed", 2), ("pollSucceeded", 3))

adProxyRolloverCause = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 6), AdProxyRolloverCauseTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverCause.setStatus('current')
if mibBuilder.loadTexts: adProxyRolloverCause.setDescription('This field indicates which specific monitored rollover condition occurred')
adSipProxyRollover = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
if mibBuilder.loadTexts: adSipProxyRollover.setStatus('current')
if mibBuilder.loadTexts: adSipProxyRollover.setDescription('This trap indicates that a SIP Proxy Monitored Rollover occured. The information about previous active server, new active server, and rollover cause is included in this trap')
adSipProxyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14))
adSipProxyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1))
adSipProxyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2))
adSipProxyFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2, 1)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationUtilityGroup"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyFullCompliance = adSipProxyFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adSipProxyFullCompliance.setDescription('The compliance statement for SNMP entities which implement version 2 of the adGenAosSipProxy MIB. When this MIB is fully implemented, then such an implementation can claim full compliance.')
adSipProxyNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 1)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyRollover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyNotificationGroup = adSipProxyNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adSipProxyNotificationGroup.setDescription('This group contains notifications about SIP Proxy Monitored Rollover occurances.')
adSipProxyNotificationUtilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 2)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyNotificationUtilityGroup = adSipProxyNotificationUtilityGroup.setStatus('current')
if mibBuilder.loadTexts: adSipProxyNotificationUtilityGroup.setDescription('A collection of objects accessible only for notifications.')
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-PROXY-MIB", adProxyRolloverFromServerInetAddressType=adProxyRolloverFromServerInetAddressType, adProxyRolloverToServerInetAddressType=adProxyRolloverToServerInetAddressType, adSipProxy=adSipProxy, adGenAOSSipProxy=adGenAOSSipProxy, adProxyRolloverFromServerInetAddress=adProxyRolloverFromServerInetAddress, adSipProxyConformance=adSipProxyConformance, adSipProxyFullCompliance=adSipProxyFullCompliance, PYSNMP_MODULE_ID=adGenAOSSipProxy, adSipProxyNotificationGroup=adSipProxyNotificationGroup, adProxyRolloverCause=adProxyRolloverCause, adSipProxyNotificationUtilityGroup=adSipProxyNotificationUtilityGroup, adSipProxyCompliances=adSipProxyCompliances, adSipProxyGroups=adSipProxyGroups, AdProxyRolloverCauseTC=AdProxyRolloverCauseTC, adSipProxyTraps=adSipProxyTraps, adProxyTimestamp=adProxyTimestamp, adSipProxyRollover=adSipProxyRollover, adProxyRolloverToServerInetAddress=adProxyRolloverToServerInetAddress)
