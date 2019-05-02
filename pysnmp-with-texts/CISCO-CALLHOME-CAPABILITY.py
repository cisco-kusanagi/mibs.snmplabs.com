#
# PySNMP MIB module CISCO-CALLHOME-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CALLHOME-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:52:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
CallHomeTransportMethod, = mibBuilder.importSymbols("CISCO-CALLHOME-MIB", "CallHomeTransportMethod")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoURLString, = mibBuilder.importSymbols("CISCO-TC", "CiscoURLString")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, Counter64, Bits, MibIdentifier, ModuleIdentity, NotificationType, Counter32, Integer32, iso, IpAddress, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Counter64", "Bits", "MibIdentifier", "ModuleIdentity", "NotificationType", "Counter32", "Integer32", "iso", "IpAddress", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoCallHomeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 355))
ciscoCallHomeCapability.setRevisions(('2012-12-05 00:00', '2011-04-14 00:00', '2010-11-10 00:00', '2009-07-10 00:00', '2009-06-17 00:00', '2009-05-07 00:00', '2008-10-27 00:00', '2007-07-30 00:00', '2006-05-10 00:00', '2004-09-20 00:00', '2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCallHomeCapability.setRevisionsDescriptions(('Added the agent capabilities statement cCallHomeCapV15R0101SYPCat6k. Updated VARIATION of ccmPeriodicAlertGroupInterval for the following agent capabilities statements: cCallHomeCapV12R0233SXHPCat6k cCallHomeCapV12R0233SXIPCat6k cCallHomeCapV12R0233SXI2PCat6k cCallHomeCapV12R0250SYPCat6k cCallHomeCapV12R0252SGPCat4k cCallHomeCapV15R0002SGPCat4K', 'Add the agent capabilities statement cCallHomeCapV15R0002SGPCat4K. Updated VARIATION of ccmAlertRateLimit for the following agent capabilities statements: cCallHomeCapV12R0233SXHPCat6k cCallHomeCapV12R0233SXIPCat6k cCallHomeCapV12R0233SXI2PCat6k cCallHomeCapV12R0250SYPCat6k cCallHomeCapV12R0252SGPCat4k', 'Add the agent capabilities statement cCallHomeCapV12R0250SYPCat6k.', 'Added the agent capabilities statement cCallHomeCapV12R0233SXI2PCat6k.', 'Updated the PRODUCT-RELEASE on agent capabilities statement cCallHomeCapV12R0252SGPCat4k.', 'Added the agent capabilities statement cCallHomeCapV12R0252SGPCat4k. Added VARIATION statements of ccmPeriodicAlertGroupEnable and ccmEventAlertGroupEnable to cCallHomeCapV12R0233SXHPCat6k and cCallHomeCapV12R0233SXIPCat6k.', 'Added the agent capabilities statement cCallHomeCapV12R0233SXIPCat6k.', 'Added the agent capabilities statement cCallHomeCapV12R0233SXHPCat6k.', "Added the agent capabilities 'cCallHomeCapSanOSV30R1MDS9000' for SanOS 3.0(1) on Cisco MDS 9000 series devices. Added ccmSmtpServerFailNotif to cCallHomeCapSanOSV20R1MDS9000.", "Added the agent capabilities 'cCallHomeCapSanOSV20R1MDS9000' for SanOS 2.0(1) on Cisco MDS 9000 series devices.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCallHomeCapability.setLastUpdated('201212050000Z')
if mibBuilder.loadTexts: ciscoCallHomeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCallHomeCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCallHomeCapability.setDescription('The capabilities description of CISCO-CALLHOME-MIB.')
cCallHomeCapCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapCatOSV08R0101Cat6k = cCallHomeCapCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapCatOSV08R0101Cat6k = cCallHomeCapCatOSV08R0101Cat6k.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapCatOSV08R0101Cat6k.setDescription('CISCO-CALLHOME-MIB capabilities.')
cCallHomeCapSanOSV20R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV20R1MDS9000 = cCallHomeCapSanOSV20R1MDS9000.setProductRelease('Cisco SanOS 2.0(1) on Cisco MDS 9000 series \n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV20R1MDS9000 = cCallHomeCapSanOSV20R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapSanOSV20R1MDS9000.setDescription('Cisco CallHome MIB capabilities')
cCallHomeCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV30R1MDS9000 = cCallHomeCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000 series \n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV30R1MDS9000 = cCallHomeCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapSanOSV30R1MDS9000.setDescription('Cisco CallHome MIB capabilities')
cCallHomeCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXHPCat6k = cCallHomeCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXHPCat6k = cCallHomeCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapV12R0233SXHPCat6k.setDescription('CISCO-CALLHOME-MIB capabilities.')
cCallHomeCapV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXIPCat6k = cCallHomeCapV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXIPCat6k = cCallHomeCapV12R0233SXIPCat6k.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapV12R0233SXIPCat6k.setDescription('CISCO-CALLHOME-MIB capabilities.')
cCallHomeCapV12R0252SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0252SGPCat4k = cCallHomeCapV12R0252SGPCat4k.setProductRelease('Cisco IOS 12.2(52)SG on Catalyst 4000 family\n                    switches, except LAN Base images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0252SGPCat4k = cCallHomeCapV12R0252SGPCat4k.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapV12R0252SGPCat4k.setDescription('CISCO-CALLHOME-MIB capabilities.')
cCallHomeCapV12R0233SXI2PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXI2PCat6k = cCallHomeCapV12R0233SXI2PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXI2PCat6k = cCallHomeCapV12R0233SXI2PCat6k.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapV12R0233SXI2PCat6k.setDescription('CISCO-CALLHOME-MIB capabilities.')
cCallHomeCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0250SYPCat6k = cCallHomeCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0250SYPCat6k = cCallHomeCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapV12R0250SYPCat6k.setDescription('CISCO-CALLHOME-MIB capabilities.')
cCallHomeCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0002SGPCat4K = cCallHomeCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Catalyst 4000 family\n                    switches, except LAN Base images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0002SGPCat4K = cCallHomeCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapV15R0002SGPCat4K.setDescription('CISCO-CALLHOME-MIB capabilities.')
cCallHomeCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0101SYPCat6k = cCallHomeCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0101SYPCat6k = cCallHomeCapV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cCallHomeCapV15R0101SYPCat6k.setDescription('CISCO-CALLHOME-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CALLHOME-CAPABILITY", cCallHomeCapCatOSV08R0101Cat6k=cCallHomeCapCatOSV08R0101Cat6k, cCallHomeCapV12R0250SYPCat6k=cCallHomeCapV12R0250SYPCat6k, PYSNMP_MODULE_ID=ciscoCallHomeCapability, cCallHomeCapSanOSV30R1MDS9000=cCallHomeCapSanOSV30R1MDS9000, cCallHomeCapV12R0233SXI2PCat6k=cCallHomeCapV12R0233SXI2PCat6k, cCallHomeCapV12R0252SGPCat4k=cCallHomeCapV12R0252SGPCat4k, ciscoCallHomeCapability=ciscoCallHomeCapability, cCallHomeCapSanOSV20R1MDS9000=cCallHomeCapSanOSV20R1MDS9000, cCallHomeCapV15R0101SYPCat6k=cCallHomeCapV15R0101SYPCat6k, cCallHomeCapV12R0233SXHPCat6k=cCallHomeCapV12R0233SXHPCat6k, cCallHomeCapV15R0002SGPCat4K=cCallHomeCapV15R0002SGPCat4K, cCallHomeCapV12R0233SXIPCat6k=cCallHomeCapV12R0233SXIPCat6k)
