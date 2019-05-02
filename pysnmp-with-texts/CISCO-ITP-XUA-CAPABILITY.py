#
# PySNMP MIB module CISCO-ITP-XUA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-XUA-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, MibIdentifier, Integer32, Counter64, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Gauge32, Counter32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Integer32", "Counter64", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Gauge32", "Counter32", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpXuaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 268))
ciscoItpXuaCapability.setRevisions(('2008-06-25 00:00', '2007-09-26 00:00', '2006-10-05 00:00', '2004-11-03 00:00', '2003-10-15 00:00', '2003-08-15 00:00', '2002-05-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpXuaCapability.setRevisionsDescriptions(('Added ciscoItpXuaCapabilityV12R0415SW, ciscoItpXuaCapabilityV12R0218IXE, ciscoItpXuaCapabilityV12R0233IRA capability statements.', 'Added ciscoItpXuaCapabilityV12R0411SW capability statement. Corrected several problems with various capability statements as follows. Modified ciscoItpXuaCapabilityV12R0225SW Modified ciscoItpXuaCapabilityV12R0219SW as follows. removed cItpXuaInstOffload removed cItpXuaInstOffloadSlot added cItpXuaSgmRemoteIpType added cItpXuaSgmRemoteIpAddr added cItpXuaSgmRemoteIpRowStatus Update ciscoItpXuaCapabilityV12R0218IXA based on changes to prior capability statements. ', 'Added ciscoItpXuaCapabilityV12R0218IXA capability statement.', 'Added ciscoItpXuaCapabilityV12R0225SW agent capability statement to support the following changes. Added the following tables. cItpXuaASRouteTable cItpXuaASRouteAsTable Added the following objects. cItpXuaAspAsWeight to cItpXuaAspAsTable cItpXuaAsNetworkAppear to cItpXuaAsTable cItpXuaAsCongLevel to cItpXuaAsTable ', 'Added ciscoItpXuaCapabilityV12R0223SW01 agent capability statement to support the following changes. Deprecated the following object. cItpXuaAspAssocId Added the following objects. cItpXuaAsNetworkName cItpXuaAspAssocIdU32', 'Added ciscoItpXuaCapabilityV12R0219SW agent capability statement to support the following changes. Added following objects and tables. cItpXuaSgmRemoteIpTable cItpXuaSgmCongLevel cItpXuaAspCongLevel Added following notifications. ciscoItpXuaAspCongChange ciscoItpXuaSgmCongChange', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpXuaCapability.setLastUpdated('200806250000Z')
if mibBuilder.loadTexts: ciscoItpXuaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpXuaCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpXuaCapability.setDescription('Agent capabilities for the CISCO-ITP-XUA-MIB.')
ciscoItpXuaCapabilityV12R0204MB5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0204MB5 = ciscoItpXuaCapabilityV12R0204MB5.setProductRelease('Cisco IOS 12.2(4)MB5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0204MB5 = ciscoItpXuaCapabilityV12R0204MB5.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0204MB5.setDescription('IOS 12.2(4)MB5 Cisco CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0219SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0219SW = ciscoItpXuaCapabilityV12R0219SW.setProductRelease('Cisco IOS 12.2(19)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0219SW = ciscoItpXuaCapabilityV12R0219SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0219SW.setDescription('IOS 12.2(19)SW Cisco CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0223SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0223SW01 = ciscoItpXuaCapabilityV12R0223SW01.setProductRelease('Cisco IOS 12.2(23)SW01')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0223SW01 = ciscoItpXuaCapabilityV12R0223SW01.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0223SW01.setDescription('IOS 12.2(23)SW01 Cisco CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0225SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0225SW = ciscoItpXuaCapabilityV12R0225SW.setProductRelease('Cisco IOS 12.2(25)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0225SW = ciscoItpXuaCapabilityV12R0225SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0225SW.setDescription('IOS 12.2(25)SW Cisco CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXA = ciscoItpXuaCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXA = ciscoItpXuaCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0411SW = ciscoItpXuaCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0411SW = ciscoItpXuaCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0415SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0415SW = ciscoItpXuaCapabilityV12R0415SW.setProductRelease('Cisco IOS 12.4(15)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0415SW = ciscoItpXuaCapabilityV12R0415SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0415SW.setDescription('Cisco IOS 12.4(15)SW CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0218IXE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXE = ciscoItpXuaCapabilityV12R0218IXE.setProductRelease('Cisco IOS 12.2(18)IXE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXE = ciscoItpXuaCapabilityV12R0218IXE.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0218IXE.setDescription('Cisco IOS 12.2(18)IXE CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0233IRA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0233IRA = ciscoItpXuaCapabilityV12R0233IRA.setProductRelease('Cisco IOS 12.2(33)IRA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0233IRA = ciscoItpXuaCapabilityV12R0233IRA.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0233IRA.setDescription('Cisco IOS 12.2(33)IRA CISCO-ITP-XUA-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-XUA-CAPABILITY", ciscoItpXuaCapabilityV12R0218IXA=ciscoItpXuaCapabilityV12R0218IXA, ciscoItpXuaCapability=ciscoItpXuaCapability, ciscoItpXuaCapabilityV12R0415SW=ciscoItpXuaCapabilityV12R0415SW, ciscoItpXuaCapabilityV12R0218IXE=ciscoItpXuaCapabilityV12R0218IXE, ciscoItpXuaCapabilityV12R0204MB5=ciscoItpXuaCapabilityV12R0204MB5, ciscoItpXuaCapabilityV12R0219SW=ciscoItpXuaCapabilityV12R0219SW, ciscoItpXuaCapabilityV12R0225SW=ciscoItpXuaCapabilityV12R0225SW, ciscoItpXuaCapabilityV12R0411SW=ciscoItpXuaCapabilityV12R0411SW, ciscoItpXuaCapabilityV12R0233IRA=ciscoItpXuaCapabilityV12R0233IRA, ciscoItpXuaCapabilityV12R0223SW01=ciscoItpXuaCapabilityV12R0223SW01, PYSNMP_MODULE_ID=ciscoItpXuaCapability)
