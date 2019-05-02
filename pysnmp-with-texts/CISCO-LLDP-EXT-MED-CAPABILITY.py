#
# PySNMP MIB module CISCO-LLDP-EXT-MED-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LLDP-EXT-MED-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:04:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, Unsigned32, iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, ModuleIdentity, MibIdentifier, IpAddress, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Unsigned32", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "ModuleIdentity", "MibIdentifier", "IpAddress", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLldpExtMedCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 584))
ciscoLldpExtMedCapability.setRevisions(('2009-12-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setLastUpdated('200912020000Z')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setDescription("This is the Agent Capabilities definition for LLDP-EXT-MED-MIB'")
lldpExtMedCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 584, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setProductRelease('Cisco IOS 12.2SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setStatus('current')
if mibBuilder.loadTexts: lldpExtMedCapability1.setDescription('LLDP MED MIB Capabilities')
mibBuilder.exportSymbols("CISCO-LLDP-EXT-MED-CAPABILITY", lldpExtMedCapability1=lldpExtMedCapability1, ciscoLldpExtMedCapability=ciscoLldpExtMedCapability, PYSNMP_MODULE_ID=ciscoLldpExtMedCapability)
