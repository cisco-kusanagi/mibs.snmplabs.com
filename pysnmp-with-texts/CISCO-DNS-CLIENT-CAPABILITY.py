#
# PySNMP MIB module CISCO-DNS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DNS-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:55:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, iso, ModuleIdentity, Bits, Integer32, Gauge32, Counter64, MibIdentifier, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "iso", "ModuleIdentity", "Bits", "Integer32", "Gauge32", "Counter64", "MibIdentifier", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDNSClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 888))
ciscoDNSClientCapability.setRevisions(('2004-11-25 00:00', '2004-08-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDNSClientCapability.setRevisionsDescriptions(("Added the agent capabilities 'cDNSClientCapSanOSV20R1MDS9000' for SanOS 2.0(1) on Cisco MDS 9000 series devices.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDNSClientCapability.setLastUpdated('200411250000Z')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setDescription('The capabilities description of CISCO-DNS-CLIENT-MIB.')
cDNSClientCapSanOSV20R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 888, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setProductRelease('Cisco SanOS 2.0(1) on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cDNSClientCapSanOSV20R1MDS9000.setDescription('Cisco DNS Client MIB capabilities')
mibBuilder.exportSymbols("CISCO-DNS-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDNSClientCapability, cDNSClientCapSanOSV20R1MDS9000=cDNSClientCapSanOSV20R1MDS9000, ciscoDNSClientCapability=ciscoDNSClientCapability)
