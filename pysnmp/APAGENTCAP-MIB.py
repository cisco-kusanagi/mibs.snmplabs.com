#
# PySNMP MIB module APAGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APAGENTCAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, Unsigned32, ModuleIdentity, mib_2, snmpModules, MibIdentifier, Counter32, enterprises, Bits, ObjectIdentity, NotificationType, Integer32, IpAddress, Counter64, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "ModuleIdentity", "mib-2", "snmpModules", "MibIdentifier", "Counter32", "enterprises", "Bits", "ObjectIdentity", "NotificationType", "Integer32", "IpAddress", "Counter64", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apAgentCapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 1))
apAgentCapModule.setRevisions(('1920-04-11 18:00', '1900-06-21 15:00', '2006-05-01 00:00', '2007-05-07 00:00', '1920-12-15 00:00', '2012-03-07 00:00', '2012-07-16 00:00',))
if mibBuilder.loadTexts: apAgentCapModule.setLastUpdated('201207160000Z')
if mibBuilder.loadTexts: apAgentCapModule.setOrganization('Acme Packet, Inc')
apSnmpMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1))
apIfMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2))
apIPMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3))
apTCPMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4))
apUDPMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5))
apEntityCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 6))
apSlogMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 7))
apSmgmtMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8))
apEnvMonitorMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9))
apSwinventoryMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 10))
apLicenseMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11))
apAmiMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 12))
apCodecMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13))
apSecurityMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14))
apH323MibCapabilites = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 15))
apSLBMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16))
apDiamMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17))
apDDMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18))
apDNSALGMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19))
apAppsMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20))
apSipMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21))
apUsbcSysMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22))
apRadiusMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23))
apSnmpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpCap = apSnmpCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpCap = apSnmpCap.setStatus('current')
apSnmpv3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setStatus('current')
apInterfacesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setStatus('current')
apIfMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setStatus('current')
apIfMibHCCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setStatus('current')
apIpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setStatus('current')
apTcpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setStatus('current')
apUdpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setStatus('current')
apEntityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setProductRelease('Acme Packet for Relase 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setStatus('current')
apSyslogCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setStatus('current')
apSmgmtCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setStatus('current')
apSmgmtCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setStatus('current')
apSmgmtCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setStatus('current')
apSmgmtCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setStatus('current')
apSmgmtCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setStatus('current')
apSmgmtCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setStatus('current')
apSmgmtNSEPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setStatus('current')
apSmgmtCtrlStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setStatus('current')
apSmgmtLDAPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setStatus('current')
apSmgmtHDRCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setStatus('current')
apSmgmtMediaSuperCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setStatus('current')
apSmgmtH248Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setStatus('current')
apSmgmtRFactorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setStatus('current')
apSmgmtSipRejectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setStatus('current')
apSmgmtDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setStatus('current')
apSmgmtRegNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setStatus('current')
apSmgmtNTPNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setStatus('current')
apSmgmtCollectorPushSuccessNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setStatus('current')
apSmgmtExtSigRealmCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setStatus('current')
apSmgmtClockNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setStatus('current')
apSmgmtRegistrationCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setStatus('current')
apSmgmtRegistrationCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setStatus('current')
apSmgmtRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setStatus('current')
apSmgmtShortSessionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setStatus('current')
apSystemManagementGatewaySynchronizedMonitorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setStatus('current')
apSmgmtRegistrationCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setStatus('current')
apSmgmtCallRecordingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setStatus('current')
apSmgmtH323AdditionsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setStatus('current')
apSmgmtENUMCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setStatus('current')
apSmgmtExtSipCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 30))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setStatus('current')
apSmgmtRealmIcmpFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 31))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setStatus('current')
apSmgmtTrapTableObjectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 32))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setStatus('current')
apSmgmtCDRPushReceiverFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 33))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setStatus('current')
apSmgmtRealmStatsQoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 34))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setStatus('current')
apSmgmtInetAddrDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 35))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setStatus('current')
apSmgmtApplicationCPUUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 36))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setStatus('current')
apSmgmtRegistrationCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 37))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setStatus('obsolete')
apSmgmtRejectedMessagesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 38))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setStatus('current')
apSmgmtEndPtDemotionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 39))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setStatus('current')
apSmgmtAdminCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 40))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setStatus('current')
apSmgmtLPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 41))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setStatus('current')
apSmgmtPhyUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 42))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setStatus('current')
apSmgmtStorageSpaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 43))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setStatus('current')
apSmgmtCtrlStatsCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 44))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setStatus('current')
apSmgmtDatabaseRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 45))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setStatus('current')
apSmgmtCallsRejectedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 46))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setStatus('current')
apSmgmtSipInterfaceRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 47))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setStatus('current')
apSmgmtRealmRegCacheSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 48))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setStatus('current')
apSmgmtSubscriptionSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 49))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setStatus('current')
apSmgmtH248PortMapUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 50))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setStatus('current')
apSmgmtDOSNotifyTrustedtoUntrustedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 51))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setStatus('current')
apSysMgmtETCUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 52))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setStatus('current')
apEnvMonCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setStatus('current')
apEnvMonCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setStatus('current')
apEnvMonPortChangeCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setStatus('current')
apEnvMonCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setStatus('current')
apSwInventoryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setStatus('current')
apLicenseCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setStatus('current')
apLicenseDatabaseRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDatabaseRegCap = apLicenseDatabaseRegCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDatabaseRegCap = apLicenseDatabaseRegCap.setStatus('current')
apLicenseExpirationWarnCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setStatus('current')
apAmiCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setStatus('current')
apCodecRealmCodecCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setStatus('current')
apCodecMediaProcessingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setStatus('current')
apCodecRealmCodecCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setStatus('current')
apCodecTranscodingStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setStatus('current')
apSecurityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setStatus('current')
apSecurityIPsecTunnelsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setStatus('current')
apSecurityIkeInterfaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setStatus('current')
apSecurityTacacsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setStatus('current')
apSecurityCertStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setStatus('current')
apSecurityIkeDDoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setStatus('current')
apSecurityCertificateCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setStatus('current')
apSecurityGtpStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setStatus('current')
apSecurityIkeInterfaceInfoCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setStatus('current')
apSecurityTacacsNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setStatus('current')
apSecurityInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setStatus('current')
apSecurityIkeDDoSInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setStatus('current')
apH323StackCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setStatus('current')
apSLBEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setStatus('current')
apSLBUntrustedEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setStatus('current')
apDiamMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setStatus('current')
apDDStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setStatus('current')
apDDNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setStatus('current')
apDDStatsGroup2Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setStatus('current')
apDDStatsGroup3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setStatus('current')
apDNSALGStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setProductRelease('Acme Packet DNS ALG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setStatus('current')
apDNSALGNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setProductRelease('Acme Packet PEC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setStatus('current')
apAppsENUMStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setStatus('current')
apAppsDNSStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setStatus('current')
apAppsENUMSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setStatus('current')
apAppsDNSSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setStatus('current')
apSipSecInterfaceRegNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setStatus('current')
apSipSecInterfaceRegObjectsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setStatus('current')
apUsbcSysCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setStatus('current')
apRadiusMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setStatus('current')
apRadiusServerStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setStatus('current')
mibBuilder.exportSymbols("APAGENTCAP-MIB", apSmgmtCtrlStatsCap2=apSmgmtCtrlStatsCap2, apSmgmtAdminCap=apSmgmtAdminCap, apSmgmtNTPNotifyCap=apSmgmtNTPNotifyCap, apSipSecInterfaceRegObjectsGroupCap=apSipSecInterfaceRegObjectsGroupCap, apEnvMonPortChangeCap=apEnvMonPortChangeCap, apSecurityCertificateCap=apSecurityCertificateCap, apEnvMonCap4=apEnvMonCap4, apIPMibCapabilities=apIPMibCapabilities, apSmgmtDOSNotifyTrustedtoUntrustedCap=apSmgmtDOSNotifyTrustedtoUntrustedCap, apSmgmtCollectorPushSuccessNotifyCap=apSmgmtCollectorPushSuccessNotifyCap, apSmgmtRegistrationCap=apSmgmtRegistrationCap, apTCPMibCapabilities=apTCPMibCapabilities, apSmgmtRealmIcmpFailureCap=apSmgmtRealmIcmpFailureCap, apSmgmtRegistrationCap3=apSmgmtRegistrationCap3, apCodecTranscodingStatsCap=apCodecTranscodingStatsCap, apAmiMibCapabilities=apAmiMibCapabilities, apSmgmtEndPtDemotionCap=apSmgmtEndPtDemotionCap, apLicenseCap=apLicenseCap, apIfMibCap=apIfMibCap, apSmgmtExtSipCap=apSmgmtExtSipCap, apSmgmtH323AdditionsCap=apSmgmtH323AdditionsCap, apH323MibCapabilites=apH323MibCapabilites, apSmgmtCap=apSmgmtCap, apUDPMibCapabilities=apUDPMibCapabilities, apSmgmtRFactorCap=apSmgmtRFactorCap, apDDStatsGroup3Cap=apDDStatsGroup3Cap, apIpCap=apIpCap, apSecurityIkeDDoSCap=apSecurityIkeDDoSCap, apSecurityIkeInterfaceCap=apSecurityIkeInterfaceCap, apLicenseMibCapabilities=apLicenseMibCapabilities, apSmgmtCap6=apSmgmtCap6, apEntityCap=apEntityCap, apLicenseExpirationWarnCap=apLicenseExpirationWarnCap, apRadiusMibCapabilities=apRadiusMibCapabilities, apDNSALGNotifGroupCap=apDNSALGNotifGroupCap, apSyslogCap=apSyslogCap, apSecurityMibCapabilities=apSecurityMibCapabilities, apEnvMonitorMibCapabilities=apEnvMonitorMibCapabilities, apSystemManagementGatewaySynchronizedMonitorCap=apSystemManagementGatewaySynchronizedMonitorCap, apSnmpMibCapabilities=apSnmpMibCapabilities, apAppsENUMStatusGroupCap=apAppsENUMStatusGroupCap, apEntityCapabilities=apEntityCapabilities, apUsbcSysMibCapabilities=apUsbcSysMibCapabilities, apDDStatsGroupCap=apDDStatsGroupCap, apUsbcSysCap=apUsbcSysCap, apInterfacesCap=apInterfacesCap, PYSNMP_MODULE_ID=apAgentCapModule, apSLBEndpointCapacityCap=apSLBEndpointCapacityCap, apIfMibHCCap=apIfMibHCCap, apSmgmtRegistrationCapacityCap=apSmgmtRegistrationCapacityCap, apDiamMibCap=apDiamMibCap, apDDNotifGroupCap=apDDNotifGroupCap, apCodecMediaProcessingCap=apCodecMediaProcessingCap, apSmgmtCap2=apSmgmtCap2, apCodecRealmCodecCap2=apCodecRealmCodecCap2, apSipSecInterfaceRegNotifGroupCap=apSipSecInterfaceRegNotifGroupCap, apAmiCap=apAmiCap, apSecurityInetCap=apSecurityInetCap, apSysMgmtETCUtilCap=apSysMgmtETCUtilCap, apSecurityIkeInterfaceInfoCap=apSecurityIkeInterfaceInfoCap, apSecurityTacacsNotifCap=apSecurityTacacsNotifCap, apSmgmtCallRecordingCap=apSmgmtCallRecordingCap, apSipMibCapabilities=apSipMibCapabilities, apAppsDNSSvrNotifGroupCap=apAppsDNSSvrNotifGroupCap, apSmgmtH248PortMapUsageCap=apSmgmtH248PortMapUsageCap, apTcpCap=apTcpCap, apSmgmtH248Cap=apSmgmtH248Cap, apAppsDNSStatusGroupCap=apAppsDNSStatusGroupCap, apSmgmtCap3=apSmgmtCap3, apSmgmtExtSigRealmCap=apSmgmtExtSigRealmCap, apSnmpv3Cap=apSnmpv3Cap, apSmgmtNSEPCap=apSmgmtNSEPCap, apSmgmtHDRCap=apSmgmtHDRCap, apDNSALGStatsGroupCap=apDNSALGStatsGroupCap, apSmgmtCallsRejectedCap=apSmgmtCallsRejectedCap, apSmgmtRegistrationCap2=apSmgmtRegistrationCap2, apIfMibCapabilities=apIfMibCapabilities, apSecurityTacacsCap=apSecurityTacacsCap, apSwInventoryCap=apSwInventoryCap, apSecurityCap=apSecurityCap, apSmgmtMediaSuperCap=apSmgmtMediaSuperCap, apUdpCap=apUdpCap, apSecurityIPsecTunnelsCap=apSecurityIPsecTunnelsCap, apRadiusServerStatsCap=apRadiusServerStatsCap, apSmgmtTrapTableObjectCap=apSmgmtTrapTableObjectCap, apEnvMonCap=apEnvMonCap, apSnmpCap=apSnmpCap, apSmgmtRegCacheLimCap=apSmgmtRegCacheLimCap, apSmgmtInetAddrDOSNotifyCap=apSmgmtInetAddrDOSNotifyCap, apAppsENUMSvrNotifGroupCap=apAppsENUMSvrNotifGroupCap, apSmgmtDOSNotifyCap=apSmgmtDOSNotifyCap, apSmgmtDatabaseRegCap=apSmgmtDatabaseRegCap, apSwinventoryMibCapabilities=apSwinventoryMibCapabilities, apSecurityGtpStatusCap=apSecurityGtpStatusCap, apRadiusMibCap=apRadiusMibCap, apSmgmtApplicationCPUUsageCap=apSmgmtApplicationCPUUsageCap, apSmgmtRealmRegCacheSummaryCap=apSmgmtRealmRegCacheSummaryCap, apSmgmtRegNotifyCap=apSmgmtRegNotifyCap, apDiamMibCapabilities=apDiamMibCapabilities, apSmgmtMibCapabilities=apSmgmtMibCapabilities, apSmgmtRealmStatsQoSCap=apSmgmtRealmStatsQoSCap, apCodecMibCapabilities=apCodecMibCapabilities, apSmgmtSipRejectCap=apSmgmtSipRejectCap, apSmgmtCap5=apSmgmtCap5, apSmgmtCDRPushReceiverFailureCap=apSmgmtCDRPushReceiverFailureCap, apAppsMibCapabilities=apAppsMibCapabilities, apH323StackCap=apH323StackCap, apSmgmtLPCap=apSmgmtLPCap, apEnvMonCap2=apEnvMonCap2, apSmgmtCtrlStatsCap=apSmgmtCtrlStatsCap, apSlogMibCapabilities=apSlogMibCapabilities, apSmgmtClockNotifyCap=apSmgmtClockNotifyCap, apSecurityCertStatusCap=apSecurityCertStatusCap, apDDStatsGroup2Cap=apDDStatsGroup2Cap, apDNSALGMibCapabilities=apDNSALGMibCapabilities, apSecurityIkeDDoSInetCap=apSecurityIkeDDoSInetCap, apSmgmtCap4=apSmgmtCap4, apSmgmtShortSessionCap=apSmgmtShortSessionCap, apSLBMibCapabilities=apSLBMibCapabilities, apSmgmtStorageSpaceCap=apSmgmtStorageSpaceCap, apSmgmtENUMCap=apSmgmtENUMCap, apSmgmtRejectedMessagesCap=apSmgmtRejectedMessagesCap, apAgentCapModule=apAgentCapModule, apSLBUntrustedEndpointCapacityCap=apSLBUntrustedEndpointCapacityCap, apCodecRealmCodecCap=apCodecRealmCodecCap, apLicenseDatabaseRegCap=apLicenseDatabaseRegCap, apSmgmtLDAPCap=apSmgmtLDAPCap, apDDMibCapabilities=apDDMibCapabilities, apSmgmtSubscriptionSummaryCap=apSmgmtSubscriptionSummaryCap, apSmgmtSipInterfaceRegCacheLimCap=apSmgmtSipInterfaceRegCacheLimCap, apSmgmtPhyUtilCap=apSmgmtPhyUtilCap)
