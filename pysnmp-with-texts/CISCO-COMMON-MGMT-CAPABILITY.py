#
# PySNMP MIB module CISCO-COMMON-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COMMON-MGMT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:53:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, Counter64, IpAddress, MibIdentifier, ObjectIdentity, Bits, iso, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "IpAddress", "MibIdentifier", "ObjectIdentity", "Bits", "iso", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCommonMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 448))
ciscoCommonMgmtCapability.setRevisions(('2005-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setLastUpdated('200508270000Z')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setDescription('Agent capabilities for CISCO-COMMON-MGMT-MIB')
ciscoCommonMgmtCapMDS30R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 448, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setStatus('current')
if mibBuilder.loadTexts: ciscoCommonMgmtCapMDS30R1.setDescription('Cisco Common Management MIB capabilities')
mibBuilder.exportSymbols("CISCO-COMMON-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoCommonMgmtCapability, ciscoCommonMgmtCapMDS30R1=ciscoCommonMgmtCapMDS30R1, ciscoCommonMgmtCapability=ciscoCommonMgmtCapability)
