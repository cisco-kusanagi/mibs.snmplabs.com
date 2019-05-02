#
# PySNMP MIB module CISCO-CSG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CSG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, Unsigned32, NotificationType, iso, TimeTicks, ModuleIdentity, Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Unsigned32", "NotificationType", "iso", "TimeTicks", "ModuleIdentity", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCsgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoCsgCapability.setRevisions(('2003-05-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCsgCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCsgCapability.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: ciscoCsgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCsgCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-csg@cisco.com')
if mibBuilder.loadTexts: ciscoCsgCapability.setDescription('Agent capabilities for the CISCO-CSG-MIB.')
ciscoCsgCapabilityV14R02ZA1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgCapabilityV14R02ZA1 = ciscoCsgCapabilityV14R02ZA1.setProductRelease('Cisco IOS 12.2(14)ZA1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgCapabilityV14R02ZA1 = ciscoCsgCapabilityV14R02ZA1.setStatus('current')
if mibBuilder.loadTexts: ciscoCsgCapabilityV14R02ZA1.setDescription('IOS 12.2(14)ZA1 Cisco CISCO-CSG-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CSG-CAPABILITY", PYSNMP_MODULE_ID=ciscoCsgCapability, ciscoCsgCapabilityV14R02ZA1=ciscoCsgCapabilityV14R02ZA1, ciscoCsgCapability=ciscoCsgCapability)
