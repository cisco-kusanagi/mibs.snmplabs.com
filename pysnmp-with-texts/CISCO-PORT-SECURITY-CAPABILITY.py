#
# PySNMP MIB module CISCO-PORT-SECURITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PORT-SECURITY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Gauge32, MibIdentifier, Bits, TimeTicks, Unsigned32, ModuleIdentity, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter32", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPortSecurityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 393))
ciscoPortSecurityCapability.setRevisions(('2005-07-14 00:00', '2004-03-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPortSecurityCapability.setRevisionsDescriptions(('Added capability statement ciscoPSecureCapV12R0218SXFPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setLastUpdated('200507140000Z')
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setDescription('The capabilities description of CISCO-PORT-SECURITY-MIB.')
ciscoPortSecurityC6kCapV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 393, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortSecurityC6kCapV08R0301 = ciscoPortSecurityC6kCapV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortSecurityC6kCapV08R0301 = ciscoPortSecurityC6kCapV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoPortSecurityC6kCapV08R0301.setDescription('CISCO-PORT-SECURITY-MIB capabilities.')
ciscoPSecureCapV12R0218SXFPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 393, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPSecureCapV12R0218SXFPCat6K = ciscoPSecureCapV12R0218SXFPCat6K.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPSecureCapV12R0218SXFPCat6K = ciscoPSecureCapV12R0218SXFPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPSecureCapV12R0218SXFPCat6K.setDescription('CISCO-PORT-SECURITY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PORT-SECURITY-CAPABILITY", ciscoPortSecurityCapability=ciscoPortSecurityCapability, ciscoPSecureCapV12R0218SXFPCat6K=ciscoPSecureCapV12R0218SXFPCat6K, ciscoPortSecurityC6kCapV08R0301=ciscoPortSecurityC6kCapV08R0301, PYSNMP_MODULE_ID=ciscoPortSecurityCapability)
