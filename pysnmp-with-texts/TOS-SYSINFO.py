#
# PySNMP MIB module TOS-SYSINFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOS-SYSINFO
# Produced by pysmi-0.3.4 at Wed May  1 15:24:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, Gauge, ModuleIdentity, Counter32, Counter64, Gauge32, Integer32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Opaque, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Gauge", "ModuleIdentity", "Counter32", "Counter64", "Gauge32", "Integer32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Opaque", "IpAddress", "NotificationType")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
tosMib, = mibBuilder.importSymbols("TOS-SMI", "tosMib")
sysInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3))
sysInfo.setRevisions(('1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sysInfo.setRevisionsDescriptions(('Initial version.', 'Creat this module,some from sysRunning, some new for tp', 'split the whole mib file into several part', 'edit the file tos-sysinfo.mib', 'add object sysSnmpVersion',))
if mibBuilder.loadTexts: sysInfo.setLastUpdated('08-03-17')
if mibBuilder.loadTexts: sysInfo.setOrganization('TOPSEC')
if mibBuilder.loadTexts: sysInfo.setContactInfo(' Topsec Beijing China E-mail: support@topsec.com.cn ')
if mibBuilder.loadTexts: sysInfo.setDescription('the product information table')
sysProductSN = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysProductSN.setStatus('current')
if mibBuilder.loadTexts: sysProductSN.setDescription('product serial number,Each device has only one psn')
sysProductType = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysProductType.setStatus('current')
if mibBuilder.loadTexts: sysProductType.setDescription("product's hardware type ")
sysSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: sysSoftwareVersion.setDescription("product's OS type and version")
sysHardwareId = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHardwareId.setStatus('current')
if mibBuilder.loadTexts: sysHardwareId.setDescription('porduct hardware ID,Each device have one and only ID')
sysSnmpVersion = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSnmpVersion.setStatus('current')
if mibBuilder.loadTexts: sysSnmpVersion.setDescription('The SNMP agent version of the system.')
sysVpnEngine = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysVpnEngine.setStatus('current')
if mibBuilder.loadTexts: sysVpnEngine.setDescription('VPN engine version of VPN module')
sysAntiVirusEngine = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAntiVirusEngine.setStatus('current')
if mibBuilder.loadTexts: sysAntiVirusEngine.setDescription('Anti-virus engine version of AV module')
sysAntiVirusLibrary = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAntiVirusLibrary.setStatus('current')
if mibBuilder.loadTexts: sysAntiVirusLibrary.setDescription('Virus define library version of AV module')
sysSecurityEngine = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityEngine.setStatus('current')
if mibBuilder.loadTexts: sysSecurityEngine.setDescription('the security engines of this device,depended on license ')
sysDpiSupport = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDpiSupport.setStatus('current')
if mibBuilder.loadTexts: sysDpiSupport.setDescription('DPI services of this device, depended on license')
sysNatSupport = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNatSupport.setStatus('current')
if mibBuilder.loadTexts: sysNatSupport.setDescription('NAT services of this device, depended on license')
sysAuthenticationSupport = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAuthenticationSupport.setStatus('current')
if mibBuilder.loadTexts: sysAuthenticationSupport.setDescription('Authentivation protocol of this device, depended on license')
sysService = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysService.setStatus('current')
if mibBuilder.loadTexts: sysService.setDescription('Services which device can support, depended on license')
sysDynamicRoutingProtocol = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDynamicRoutingProtocol.setStatus('current')
if mibBuilder.loadTexts: sysDynamicRoutingProtocol.setDescription('Dynamic routing protocol that device support, depended on license')
sysMaxSession = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMaxSession.setStatus('current')
if mibBuilder.loadTexts: sysMaxSession.setDescription('Max session that device support, depended on license')
sysMaxVrcClient = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMaxVrcClient.setStatus('current')
if mibBuilder.loadTexts: sysMaxVrcClient.setDescription(' Max vrc client that device support, depended on license')
mibBuilder.exportSymbols("TOS-SYSINFO", sysSecurityEngine=sysSecurityEngine, sysProductSN=sysProductSN, sysVpnEngine=sysVpnEngine, sysMaxVrcClient=sysMaxVrcClient, sysSnmpVersion=sysSnmpVersion, sysProductType=sysProductType, sysHardwareId=sysHardwareId, sysNatSupport=sysNatSupport, PYSNMP_MODULE_ID=sysInfo, sysAntiVirusLibrary=sysAntiVirusLibrary, sysService=sysService, sysAntiVirusEngine=sysAntiVirusEngine, sysAuthenticationSupport=sysAuthenticationSupport, sysMaxSession=sysMaxSession, sysDynamicRoutingProtocol=sysDynamicRoutingProtocol, sysSoftwareVersion=sysSoftwareVersion, sysDpiSupport=sysDpiSupport, sysInfo=sysInfo)
