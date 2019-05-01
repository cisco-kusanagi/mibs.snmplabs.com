#
# PySNMP MIB module CISCO-RTTMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RTTMON-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:11:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, ModuleIdentity, Bits, ObjectIdentity, Unsigned32, Counter32, NotificationType, Gauge32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Bits", "ObjectIdentity", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRttMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 62))
ciscoRttMonCapability.setRevisions(('2006-03-02 00:00', '2005-12-14 00:00', '2005-06-09 00:00', '2005-05-01 00:00', '2004-05-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRttMonCapability.setRevisionsDescriptions(('Added capability definition ciscoRttMonCapV12R0201SRB for 12.2(01)SRB', 'Agent capabilities for CISCO-RTTMON-MIB on CRS-1 IOS-XR Release 3.3', 'Added capability definition ciscoRttMonCapV12R0403rdT for 12.4(3rd)T', 'Added capability definition ciscoRttMonCapV12R0402ndT for 12.4(2nd)T and ciscoRttMonCapV12R0206thSX for 12.2(6th)SX', 'Initial Creation',))
if mibBuilder.loadTexts: ciscoRttMonCapability.setLastUpdated('200603020000Z')
if mibBuilder.loadTexts: ciscoRttMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRttMonCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoRttMonCapability.setDescription('Agent capabilities for CISCO-RTTMON-MIB')
ciscoRttMonCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setProductRelease('Cisco IOS 12.3(6th)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapabilityRev1.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapV12R0402ndT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setProductRelease('Cisco IOS 12.4(2nd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0402ndT.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapV12R0206thSX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setProductRelease('Cisco IOS 12.2(6th)SX')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0206thSX.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapV12R0403rdT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setProductRelease('Cisco IOS 12.4(3rd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0403rdT.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapCRS1V3R3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setProductRelease('Cisco IOS XR release 3.3 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapCRS1V3R3.setDescription('Cisco RTTMON MIB capabilities.')
ciscoRttMonCapV12R0201SRB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0201SRB.setDescription('Cisco RTTMON MIB capabilities')
mibBuilder.exportSymbols("CISCO-RTTMON-CAPABILITY", ciscoRttMonCapabilityRev1=ciscoRttMonCapabilityRev1, ciscoRttMonCapability=ciscoRttMonCapability, ciscoRttMonCapV12R0206thSX=ciscoRttMonCapV12R0206thSX, ciscoRttMonCapCRS1V3R3=ciscoRttMonCapCRS1V3R3, PYSNMP_MODULE_ID=ciscoRttMonCapability, ciscoRttMonCapV12R0402ndT=ciscoRttMonCapV12R0402ndT, ciscoRttMonCapV12R0201SRB=ciscoRttMonCapV12R0201SRB, ciscoRttMonCapV12R0403rdT=ciscoRttMonCapV12R0403rdT)
