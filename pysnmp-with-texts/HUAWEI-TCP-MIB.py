#
# PySNMP MIB module HUAWEI-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, ObjectIdentity, Integer32, Bits, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, iso, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "ObjectIdentity", "Integer32", "Bits", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "iso", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tcpConnLocalPort, tcpConnLocalAddress, tcpConnRemAddress, tcpConnRemPort = mibBuilder.importSymbols("TCP-MIB", "tcpConnLocalPort", "tcpConnLocalAddress", "tcpConnRemAddress", "tcpConnRemPort")
hwTCP = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34))
if mibBuilder.loadTexts: hwTCP.setLastUpdated('200406260000Z')
if mibBuilder.loadTexts: hwTCP.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwTCP.setContactInfo(' R&D Beijing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwTCP.setDescription('The HUAWEI-TCP-MIB provides information about TCP. Now only trap for MD5 authentication failures is provided, which include local address, local port, remote address, remote port. When MD5 authentication fails, the trap will send.')
hwTCPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1))
hwTCPProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwTCPProtocol.setStatus('current')
if mibBuilder.loadTexts: hwTCPProtocol.setDescription('This variable indicates which protocol use MD5 authentication. If protocol is BGP, this variable will be the BGP string; If protocol is LDP, this variable will be the LDP string; If protocol is unknown, this variable will be the Unknown protocol string.')
hwTCPVrfName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwTCPVrfName.setStatus('current')
if mibBuilder.loadTexts: hwTCPVrfName.setDescription('This variable indicates which VPN the TCP connection belongs to. If the TCP connection belongs to public net, this variable is null.')
hwTCPTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 2))
hwTCPMD5AuthenFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 2, 1)).setObjects(("TCP-MIB", "tcpConnLocalAddress"), ("TCP-MIB", "tcpConnLocalPort"), ("TCP-MIB", "tcpConnRemAddress"), ("TCP-MIB", "tcpConnRemPort"), ("HUAWEI-TCP-MIB", "hwTCPProtocol"), ("HUAWEI-TCP-MIB", "hwTCPVrfName"))
if mibBuilder.loadTexts: hwTCPMD5AuthenFail.setStatus('current')
if mibBuilder.loadTexts: hwTCPMD5AuthenFail.setDescription('This trap indicates that the MD5 authentication fails. the information include local address, port, remote address, port, protocol and VRF name. When MD5 authentication fails, this trap will be sent.')
hwTCPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3))
hwTCPCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 1))
hwTCPCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 1, 1)).setObjects(("HUAWEI-TCP-MIB", "hwTCPTrapGroup"), ("HUAWEI-TCP-MIB", "hwTCPForTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTCPCompliance = hwTCPCompliance.setStatus('current')
if mibBuilder.loadTexts: hwTCPCompliance.setDescription('The compliance statement for entities which implement the Huawei TCP MIB.')
hwTCPGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2))
hwTCPTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2, 1)).setObjects(("HUAWEI-TCP-MIB", "hwTCPMD5AuthenFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTCPTrapGroup = hwTCPTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwTCPTrapGroup.setDescription('A collection of objects providing mandatory TCP trap information.')
hwTCPForTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2, 2)).setObjects(("HUAWEI-TCP-MIB", "hwTCPProtocol"), ("HUAWEI-TCP-MIB", "hwTCPVrfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTCPForTrapGroup = hwTCPForTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwTCPForTrapGroup.setDescription('These objects are required for entities which support notification applications.')
mibBuilder.exportSymbols("HUAWEI-TCP-MIB", hwTCPForTrapGroup=hwTCPForTrapGroup, PYSNMP_MODULE_ID=hwTCP, hwTCPTrapGroup=hwTCPTrapGroup, hwTCPGroups=hwTCPGroups, hwTCPProtocol=hwTCPProtocol, hwTCP=hwTCP, hwTCPCompliance=hwTCPCompliance, hwTCPConformance=hwTCPConformance, hwTCPTraps=hwTCPTraps, hwTCPCompliances=hwTCPCompliances, hwTCPMD5AuthenFail=hwTCPMD5AuthenFail, hwTCPObjects=hwTCPObjects, hwTCPVrfName=hwTCPVrfName)
