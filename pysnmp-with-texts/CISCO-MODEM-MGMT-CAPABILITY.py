#
# PySNMP MIB module CISCO-MODEM-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MODEM-MGMT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, IpAddress, Gauge32, Bits, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ObjectIdentity, MibIdentifier, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "IpAddress", "Gauge32", "Bits", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoModemMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoModemMgmtCapability.setRevisions(('2006-07-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoModemMgmtCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setLastUpdated('200607310000Z')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setDescription('Agent capabilities for CISCO-MODEM-MGMT-MIB.')
ciscoModemMgmtCapV12R4TISR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setProductRelease('Cisco IOS 12.4 for ATG Platform Devices')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setStatus('current')
if mibBuilder.loadTexts: ciscoModemMgmtCapV12R4TISR.setDescription('CISCO-MODEM-MGMT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODEM-MGMT-CAPABILITY", ciscoModemMgmtCapV12R4TISR=ciscoModemMgmtCapV12R4TISR, ciscoModemMgmtCapability=ciscoModemMgmtCapability, PYSNMP_MODULE_ID=ciscoModemMgmtCapability)
