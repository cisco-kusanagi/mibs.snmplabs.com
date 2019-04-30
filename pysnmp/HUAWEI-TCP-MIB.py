#
# PySNMP MIB module HUAWEI-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Counter64, ObjectIdentity, MibIdentifier, Counter32, IpAddress, ModuleIdentity, Integer32, Gauge32, Unsigned32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32", "IpAddress", "ModuleIdentity", "Integer32", "Gauge32", "Unsigned32", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tcpConnRemAddress, tcpConnRemPort, tcpConnLocalAddress, tcpConnLocalPort = mibBuilder.importSymbols("TCP-MIB", "tcpConnRemAddress", "tcpConnRemPort", "tcpConnLocalAddress", "tcpConnLocalPort")
hwTCP = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34))
if mibBuilder.loadTexts: hwTCP.setLastUpdated('200406260000Z')
if mibBuilder.loadTexts: hwTCP.setOrganization('Huawei Technologies co.,Ltd.')
hwTCPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1))
hwTCPProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwTCPProtocol.setStatus('current')
hwTCPVrfName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwTCPVrfName.setStatus('current')
hwTCPTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 2))
hwTCPMD5AuthenFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 2, 1)).setObjects(("TCP-MIB", "tcpConnLocalAddress"), ("TCP-MIB", "tcpConnLocalPort"), ("TCP-MIB", "tcpConnRemAddress"), ("TCP-MIB", "tcpConnRemPort"), ("HUAWEI-TCP-MIB", "hwTCPProtocol"), ("HUAWEI-TCP-MIB", "hwTCPVrfName"))
if mibBuilder.loadTexts: hwTCPMD5AuthenFail.setStatus('current')
hwTCPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3))
hwTCPCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 1))
hwTCPCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 1, 1)).setObjects(("HUAWEI-TCP-MIB", "hwTCPTrapGroup"), ("HUAWEI-TCP-MIB", "hwTCPForTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTCPCompliance = hwTCPCompliance.setStatus('current')
hwTCPGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2))
hwTCPTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2, 1)).setObjects(("HUAWEI-TCP-MIB", "hwTCPMD5AuthenFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTCPTrapGroup = hwTCPTrapGroup.setStatus('current')
hwTCPForTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2, 2)).setObjects(("HUAWEI-TCP-MIB", "hwTCPProtocol"), ("HUAWEI-TCP-MIB", "hwTCPVrfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTCPForTrapGroup = hwTCPForTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-TCP-MIB", hwTCPObjects=hwTCPObjects, hwTCPMD5AuthenFail=hwTCPMD5AuthenFail, hwTCPTraps=hwTCPTraps, hwTCPConformance=hwTCPConformance, hwTCPGroups=hwTCPGroups, hwTCPForTrapGroup=hwTCPForTrapGroup, hwTCPTrapGroup=hwTCPTrapGroup, hwTCPVrfName=hwTCPVrfName, PYSNMP_MODULE_ID=hwTCP, hwTCPProtocol=hwTCPProtocol, hwTCP=hwTCP, hwTCPCompliances=hwTCPCompliances, hwTCPCompliance=hwTCPCompliance)
