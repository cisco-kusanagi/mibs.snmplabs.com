#
# PySNMP MIB module CISCO-IKE-FLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IKE-FLOW-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, Unsigned32, MibIdentifier, Integer32, Bits, Counter64, ModuleIdentity, Counter32, IpAddress, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "Integer32", "Bits", "Counter64", "ModuleIdentity", "Counter32", "IpAddress", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIkeFlowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 487))
ciscoIkeFlowCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIkeFlowCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setDescription('Agent capabilities for CISCO-IKE-FLOW-MIB.')
ciscoIkeFlowCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 487, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowCapSanOSV30R1MDS9000 = ciscoIkeFlowCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowCapSanOSV30R1MDS9000 = ciscoIkeFlowCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIkeFlowCapSanOSV30R1MDS9000.setDescription('Cisco IKE Flow Monitoring MIB capabilities')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoIkeFlowCapability, ciscoIkeFlowCapSanOSV30R1MDS9000=ciscoIkeFlowCapSanOSV30R1MDS9000, ciscoIkeFlowCapability=ciscoIkeFlowCapability)
