#
# PySNMP MIB module APAGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APAGENTCAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, ObjectIdentity, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, snmpModules, Gauge32, mib_2, TimeTicks, Integer32, Unsigned32, MibIdentifier, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ObjectIdentity", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "snmpModules", "Gauge32", "mib-2", "TimeTicks", "Integer32", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apAgentCapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 1))
apAgentCapModule.setRevisions(('1920-04-11 18:00', '1900-06-21 15:00', '2006-05-01 00:00', '2007-05-07 00:00', '1920-12-15 00:00', '2012-03-07 00:00', '2012-07-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apAgentCapModule.setRevisionsDescriptions((' Add agent capacity for release 2.0. ', ' The agent capability MIB for Acme Packet', ' Add agent capability for SD9000 series', ' Add agent capability for SD9000 series', ' Add agent capability for ap-dd.mib', ' Add agent capability for ap-apps.mib', 'Updated contact information.',))
if mibBuilder.loadTexts: apAgentCapModule.setLastUpdated('201207160000Z')
if mibBuilder.loadTexts: apAgentCapModule.setOrganization('Acme Packet, Inc')
if mibBuilder.loadTexts: apAgentCapModule.setContactInfo(' Customer Service Postal: Acme Packet, Inc 100 Crosby Drive Bedford, MA 01730 US Tel: 1-781-328-4400 E-mail: support@acmepacket.com')
if mibBuilder.loadTexts: apAgentCapModule.setDescription('Add agent capacity for release 3.0. Modified: ifGroup.')
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
if mibBuilder.loadTexts: apSnmpCap.setDescription('Acme Packet Agent Capability for SNMPv2-MIB.')
apSnmpv3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setStatus('current')
if mibBuilder.loadTexts: apSnmpv3Cap.setDescription('Acme Packet Agent Capability for SNMPv3 MIBs.')
apInterfacesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setStatus('current')
if mibBuilder.loadTexts: apInterfacesCap.setDescription('Acme Packet Agent Capability for interfaces.')
apIfMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setStatus('current')
if mibBuilder.loadTexts: apIfMibCap.setDescription('Acme Packet Agent Capability IfMib support.')
apIfMibHCCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setStatus('current')
if mibBuilder.loadTexts: apIfMibHCCap.setDescription('Acme Packet Agent Capability for interfaces.')
apIpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setStatus('current')
if mibBuilder.loadTexts: apIpCap.setDescription('Acme Packet Agent Capability IP support.')
apTcpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setStatus('current')
if mibBuilder.loadTexts: apTcpCap.setDescription('Acme Packet Agent Capability TCP support.')
apUdpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setStatus('current')
if mibBuilder.loadTexts: apUdpCap.setDescription('Acme Packet Agent Capability UDP support.')
apEntityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setProductRelease('Acme Packet for Relase 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setStatus('current')
if mibBuilder.loadTexts: apEntityCap.setDescription('Acme Packet Agent Capability for entity MIB.')
apSyslogCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setStatus('current')
if mibBuilder.loadTexts: apSyslogCap.setDescription('Acme Packet Agent Capability for enterprise syslog MIB.')
apSmgmtCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap2.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap3.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap4.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap5.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap6.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtNSEPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtNSEPCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtCtrlStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCtrlStatsCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtLDAPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtLDAPCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtHDRCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtHDRCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtMediaSuperCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtMediaSuperCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtH248Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtH248Cap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtRFactorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRFactorCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtSipRejectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtSipRejectCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtDOSNotifyCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtRegNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegNotifyCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtNTPNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtNTPNotifyCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtCollectorPushSuccessNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCollectorPushSuccessNotifyCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtExtSigRealmCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtExtSigRealmCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtClockNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtClockNotifyCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtRegistrationCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegistrationCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtRegistrationCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegistrationCap2.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegCacheLimCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtShortSessionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtShortSessionCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSystemManagementGatewaySynchronizedMonitorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setStatus('current')
if mibBuilder.loadTexts: apSystemManagementGatewaySynchronizedMonitorCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtRegistrationCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegistrationCap3.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtCallRecordingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCallRecordingCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtH323AdditionsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtH323AdditionsCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtENUMCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtENUMCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtExtSipCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 30))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtExtSipCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtRealmIcmpFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 31))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRealmIcmpFailureCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtTrapTableObjectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 32))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtTrapTableObjectCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtCDRPushReceiverFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 33))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCDRPushReceiverFailureCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtRealmStatsQoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 34))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRealmStatsQoSCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtInetAddrDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 35))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtInetAddrDOSNotifyCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtApplicationCPUUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 36))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtApplicationCPUUsageCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtRegistrationCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 37))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setStatus('obsolete')
if mibBuilder.loadTexts: apSmgmtRegistrationCapacityCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtRejectedMessagesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 38))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRejectedMessagesCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtEndPtDemotionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 39))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtEndPtDemotionCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtAdminCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 40))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtAdminCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtLPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 41))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtLPCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtPhyUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 42))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtPhyUtilCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtStorageSpaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 43))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtStorageSpaceCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtCtrlStatsCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 44))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCtrlStatsCap2.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtDatabaseRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 45))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtDatabaseRegCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtCallsRejectedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 46))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCallsRejectedCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSmgmtSipInterfaceRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 47))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtSipInterfaceRegCacheLimCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtRealmRegCacheSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 48))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRealmRegCacheSummaryCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtSubscriptionSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 49))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtSubscriptionSummaryCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtH248PortMapUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 50))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtH248PortMapUsageCap.setDescription('Acme Packet Agent Capability for enterprise system management MIB.')
apSmgmtDOSNotifyTrustedtoUntrustedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 51))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtDOSNotifyTrustedtoUntrustedCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apSysMgmtETCUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 52))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSysMgmtETCUtilCap.setDescription('Acme Packet Agent Capability for enterprise system mamgerment MIB.')
apEnvMonCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setStatus('current')
if mibBuilder.loadTexts: apEnvMonCap.setDescription('Acme Packet Agent Capability for enterprise Environmental Monitor MIB.')
apEnvMonCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setStatus('current')
if mibBuilder.loadTexts: apEnvMonCap2.setDescription('Acme Packet Agent Capability for enterprise Environmental Monitor MIB.')
apEnvMonPortChangeCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setStatus('current')
if mibBuilder.loadTexts: apEnvMonPortChangeCap.setDescription('Acme Packet Agent Capability for enterprise Environmental Monitor MIB.')
apEnvMonCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setStatus('current')
if mibBuilder.loadTexts: apEnvMonCap4.setDescription('Acme Packet Agent Capability for enterprise Environmental Monitor MIB.')
apSwInventoryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setStatus('current')
if mibBuilder.loadTexts: apSwInventoryCap.setDescription('Acme Packet Agent Capability for enterprise software inventory MIB.')
apLicenseCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setStatus('current')
if mibBuilder.loadTexts: apLicenseCap.setDescription('Acme Packet Agent Capability for enterprise License MIB.')
apLicenseDatabaseRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDatabaseRegCap = apLicenseDatabaseRegCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDatabaseRegCap = apLicenseDatabaseRegCap.setStatus('current')
if mibBuilder.loadTexts: apLicenseDatabaseRegCap.setDescription('Acme Packet Agent Capability for enterprise License MIB.')
apLicenseExpirationWarnCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setStatus('current')
if mibBuilder.loadTexts: apLicenseExpirationWarnCap.setDescription('Acme Packet Agent Capability for enterprise License MIB.')
apAmiCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setStatus('current')
if mibBuilder.loadTexts: apAmiCap.setDescription('Acme Packet Agent Capability for enterprise AMI MIB.')
apCodecRealmCodecCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap.setDescription('Acme Packet Agent Capability for enterprise codec MIB.')
apCodecMediaProcessingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setStatus('current')
if mibBuilder.loadTexts: apCodecMediaProcessingCap.setDescription('Acme Packet Agent Capability for enterprise codec MIB.')
apCodecRealmCodecCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap2.setDescription('Acme Packet Agent Capability for enterprise codec MIB. (Additional Codecs)')
apCodecTranscodingStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setStatus('current')
if mibBuilder.loadTexts: apCodecTranscodingStatsCap.setDescription('Acme Packet Agent Capability for enterprise codec MIB. (Additional Codecs)')
apSecurityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityCap.setDescription('Acme Packet Agent Capability for enterprise License MIB.')
apSecurityIPsecTunnelsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIPsecTunnelsCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityIkeInterfaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityTacacsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTacacsCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityCertStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityCertStatusCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityIkeDDoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeDDoSCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityCertificateCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityCertificateCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityGtpStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityGtpStatusCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityIkeInterfaceInfoCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceInfoCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityTacacsNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTacacsNotifCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apSecurityInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityInetCap.setDescription('Acme Packet Agent Capability for enterprise License MIB.')
apSecurityIkeDDoSInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeDDoSInetCap.setDescription('Acme Packet Agent Capability for enterprise Security MIB.')
apH323StackCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setStatus('current')
if mibBuilder.loadTexts: apH323StackCap.setDescription('Acme Packet Agent Capability for H323 stack.')
apSLBEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setStatus('current')
if mibBuilder.loadTexts: apSLBEndpointCapacityCap.setDescription('Acme Packet Agent Capability for enterprise SLB MIB.')
apSLBUntrustedEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setStatus('current')
if mibBuilder.loadTexts: apSLBUntrustedEndpointCapacityCap.setDescription('Acme Packet Agent Capability for enterprise SLB MIB.')
apDiamMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setStatus('current')
if mibBuilder.loadTexts: apDiamMibCap.setDescription('Acme Packet Capability for AP-DIAMETER-MIB.')
apDDStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDDStatsGroupCap.setDescription('Acme Packet Agent Capability for enterprise DD MIB.')
apDDNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDDNotifGroupCap.setDescription('Acme Packet Agent Capability for enterprise DD MIB.')
apDDStatsGroup2Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setStatus('current')
if mibBuilder.loadTexts: apDDStatsGroup2Cap.setDescription('Acme Packet Agent Capability for enterprise DD MIB.')
apDDStatsGroup3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setStatus('current')
if mibBuilder.loadTexts: apDDStatsGroup3Cap.setDescription('Acme Packet Agent Capability for enterprise DD MIB.')
apDNSALGStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setProductRelease('Acme Packet DNS ALG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDNSALGStatsGroupCap.setDescription('Acme Packet Agent Capability for enterprise DNSALG MIB.')
apDNSALGNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setProductRelease('Acme Packet PEC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDNSALGNotifGroupCap.setDescription('Acme Packet Agent Capability for enterprise DNSALG MIB.')
apAppsENUMStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsENUMStatusGroupCap.setDescription('Acme Packet Agent Capability for APPS ENUM server status group. ')
apAppsDNSStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsDNSStatusGroupCap.setDescription('Acme Packet Agent Capability for APPS DNS server status group. ')
apAppsENUMSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsENUMSvrNotifGroupCap.setDescription('Acme Packet Agent Capability for APPS ENUM Server Notif group.')
apAppsDNSSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsDNSSvrNotifGroupCap.setDescription('Acme Packet Agent Capability for APPS DNS Server Notif group.')
apSipSecInterfaceRegNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipSecInterfaceRegNotifGroupCap.setDescription('Acme Packet Agent Capability for SIP Secondary SIP Interface Registrations Notif group.')
apSipSecInterfaceRegObjectsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipSecInterfaceRegObjectsGroupCap.setDescription('Acme Packet Agent Capability for SIP Secondary SIP Interface Registrations Object group.')
apUsbcSysCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysCap.setDescription('Acme Packet Agent Capability for USBC system mamgerment MIB.')
apRadiusMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setStatus('current')
if mibBuilder.loadTexts: apRadiusMibCap.setDescription('Acme Packet Capability for AP-RADIUS-MIB.')
apRadiusServerStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setProductRelease('Acme Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerStatsCap.setDescription('Acme Packet Capability for AP-RADIUS-MIB.')
mibBuilder.exportSymbols("APAGENTCAP-MIB", apSmgmtCap3=apSmgmtCap3, apSmgmtRejectedMessagesCap=apSmgmtRejectedMessagesCap, apInterfacesCap=apInterfacesCap, apSipSecInterfaceRegObjectsGroupCap=apSipSecInterfaceRegObjectsGroupCap, apSmgmtNTPNotifyCap=apSmgmtNTPNotifyCap, apSmgmtTrapTableObjectCap=apSmgmtTrapTableObjectCap, apEnvMonPortChangeCap=apEnvMonPortChangeCap, apSLBUntrustedEndpointCapacityCap=apSLBUntrustedEndpointCapacityCap, apDNSALGMibCapabilities=apDNSALGMibCapabilities, apSmgmtRealmStatsQoSCap=apSmgmtRealmStatsQoSCap, apSecurityCertStatusCap=apSecurityCertStatusCap, apSyslogCap=apSyslogCap, apRadiusMibCap=apRadiusMibCap, apIfMibCap=apIfMibCap, apDiamMibCap=apDiamMibCap, apSmgmtRegNotifyCap=apSmgmtRegNotifyCap, apSmgmtRegistrationCap3=apSmgmtRegistrationCap3, apSmgmtAdminCap=apSmgmtAdminCap, apAmiCap=apAmiCap, apCodecRealmCodecCap2=apCodecRealmCodecCap2, apEnvMonCap2=apEnvMonCap2, apLicenseDatabaseRegCap=apLicenseDatabaseRegCap, apSmgmtH248PortMapUsageCap=apSmgmtH248PortMapUsageCap, apIPMibCapabilities=apIPMibCapabilities, apCodecTranscodingStatsCap=apCodecTranscodingStatsCap, apSmgmtEndPtDemotionCap=apSmgmtEndPtDemotionCap, apSmgmtH248Cap=apSmgmtH248Cap, apSmgmtSipInterfaceRegCacheLimCap=apSmgmtSipInterfaceRegCacheLimCap, apSmgmtClockNotifyCap=apSmgmtClockNotifyCap, apLicenseMibCapabilities=apLicenseMibCapabilities, apSmgmtCallRecordingCap=apSmgmtCallRecordingCap, apSmgmtRegCacheLimCap=apSmgmtRegCacheLimCap, apSmgmtCDRPushReceiverFailureCap=apSmgmtCDRPushReceiverFailureCap, apSecurityMibCapabilities=apSecurityMibCapabilities, apSmgmtENUMCap=apSmgmtENUMCap, apAppsENUMSvrNotifGroupCap=apAppsENUMSvrNotifGroupCap, apSmgmtHDRCap=apSmgmtHDRCap, apSmgmtDOSNotifyCap=apSmgmtDOSNotifyCap, apTCPMibCapabilities=apTCPMibCapabilities, apSmgmtRegistrationCapacityCap=apSmgmtRegistrationCapacityCap, apAppsENUMStatusGroupCap=apAppsENUMStatusGroupCap, apSmgmtStorageSpaceCap=apSmgmtStorageSpaceCap, apSystemManagementGatewaySynchronizedMonitorCap=apSystemManagementGatewaySynchronizedMonitorCap, apSmgmtCap4=apSmgmtCap4, apDDNotifGroupCap=apDDNotifGroupCap, apSmgmtCap6=apSmgmtCap6, apUsbcSysMibCapabilities=apUsbcSysMibCapabilities, apSmgmtH323AdditionsCap=apSmgmtH323AdditionsCap, apSmgmtPhyUtilCap=apSmgmtPhyUtilCap, apSecurityCertificateCap=apSecurityCertificateCap, apSecurityIkeInterfaceCap=apSecurityIkeInterfaceCap, apEntityCap=apEntityCap, apSecurityTacacsCap=apSecurityTacacsCap, apDDStatsGroup2Cap=apDDStatsGroup2Cap, apSmgmtCap5=apSmgmtCap5, apSmgmtInetAddrDOSNotifyCap=apSmgmtInetAddrDOSNotifyCap, apSmgmtRegistrationCap=apSmgmtRegistrationCap, apSLBMibCapabilities=apSLBMibCapabilities, apSecurityIkeDDoSCap=apSecurityIkeDDoSCap, apSwInventoryCap=apSwInventoryCap, apSwinventoryMibCapabilities=apSwinventoryMibCapabilities, apSecurityTacacsNotifCap=apSecurityTacacsNotifCap, apSmgmtDatabaseRegCap=apSmgmtDatabaseRegCap, apSmgmtCtrlStatsCap=apSmgmtCtrlStatsCap, apSmgmtApplicationCPUUsageCap=apSmgmtApplicationCPUUsageCap, apSmgmtLPCap=apSmgmtLPCap, apRadiusServerStatsCap=apRadiusServerStatsCap, apSnmpv3Cap=apSnmpv3Cap, apSmgmtSubscriptionSummaryCap=apSmgmtSubscriptionSummaryCap, apSecurityInetCap=apSecurityInetCap, apSmgmtRFactorCap=apSmgmtRFactorCap, apH323StackCap=apH323StackCap, apAppsMibCapabilities=apAppsMibCapabilities, apSmgmtShortSessionCap=apSmgmtShortSessionCap, apIfMibHCCap=apIfMibHCCap, apSmgmtCtrlStatsCap2=apSmgmtCtrlStatsCap2, apUDPMibCapabilities=apUDPMibCapabilities, apIpCap=apIpCap, apSmgmtRealmIcmpFailureCap=apSmgmtRealmIcmpFailureCap, apSmgmtExtSipCap=apSmgmtExtSipCap, apSipSecInterfaceRegNotifGroupCap=apSipSecInterfaceRegNotifGroupCap, apUsbcSysCap=apUsbcSysCap, apSmgmtLDAPCap=apSmgmtLDAPCap, apIfMibCapabilities=apIfMibCapabilities, apSmgmtNSEPCap=apSmgmtNSEPCap, apSLBEndpointCapacityCap=apSLBEndpointCapacityCap, apCodecMibCapabilities=apCodecMibCapabilities, apLicenseExpirationWarnCap=apLicenseExpirationWarnCap, apUdpCap=apUdpCap, apSmgmtMediaSuperCap=apSmgmtMediaSuperCap, apDDStatsGroupCap=apDDStatsGroupCap, apCodecRealmCodecCap=apCodecRealmCodecCap, apTcpCap=apTcpCap, apSysMgmtETCUtilCap=apSysMgmtETCUtilCap, apSmgmtCallsRejectedCap=apSmgmtCallsRejectedCap, apSipMibCapabilities=apSipMibCapabilities, apSecurityGtpStatusCap=apSecurityGtpStatusCap, apSmgmtDOSNotifyTrustedtoUntrustedCap=apSmgmtDOSNotifyTrustedtoUntrustedCap, apSecurityIkeDDoSInetCap=apSecurityIkeDDoSInetCap, apDNSALGStatsGroupCap=apDNSALGStatsGroupCap, apSmgmtSipRejectCap=apSmgmtSipRejectCap, apCodecMediaProcessingCap=apCodecMediaProcessingCap, apH323MibCapabilites=apH323MibCapabilites, PYSNMP_MODULE_ID=apAgentCapModule, apSmgmtCap=apSmgmtCap, apAppsDNSStatusGroupCap=apAppsDNSStatusGroupCap, apRadiusMibCapabilities=apRadiusMibCapabilities, apSmgmtCap2=apSmgmtCap2, apDDMibCapabilities=apDDMibCapabilities, apSecurityIkeInterfaceInfoCap=apSecurityIkeInterfaceInfoCap, apEnvMonCap=apEnvMonCap, apSecurityCap=apSecurityCap, apSmgmtCollectorPushSuccessNotifyCap=apSmgmtCollectorPushSuccessNotifyCap, apEnvMonCap4=apEnvMonCap4, apAppsDNSSvrNotifGroupCap=apAppsDNSSvrNotifGroupCap, apSnmpCap=apSnmpCap, apAgentCapModule=apAgentCapModule, apDiamMibCapabilities=apDiamMibCapabilities, apSmgmtRegistrationCap2=apSmgmtRegistrationCap2, apSnmpMibCapabilities=apSnmpMibCapabilities, apSecurityIPsecTunnelsCap=apSecurityIPsecTunnelsCap, apSmgmtExtSigRealmCap=apSmgmtExtSigRealmCap, apLicenseCap=apLicenseCap, apSmgmtMibCapabilities=apSmgmtMibCapabilities, apSlogMibCapabilities=apSlogMibCapabilities, apSmgmtRealmRegCacheSummaryCap=apSmgmtRealmRegCacheSummaryCap, apAmiMibCapabilities=apAmiMibCapabilities, apDDStatsGroup3Cap=apDDStatsGroup3Cap, apDNSALGNotifGroupCap=apDNSALGNotifGroupCap, apEntityCapabilities=apEntityCapabilities, apEnvMonitorMibCapabilities=apEnvMonitorMibCapabilities)
