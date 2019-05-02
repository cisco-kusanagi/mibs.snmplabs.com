#
# PySNMP MIB module DPI20-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DPI20-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:54:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Counter64, IpAddress, Unsigned32, TimeTicks, ModuleIdentity, ObjectIdentity, MibIdentifier, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dpi20MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2, 2, 1))
dpi20MIB.setRevisions(('1996-09-30 00:00', '1996-05-01 00:00', '1995-05-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dpi20MIB.setRevisionsDescriptions(('Changes in this revision - Added dpiPathNameForUnixStream ', 'Changes in this revision - Change telephone number', 'Changes in this revision - Enable SNMPv2 items - import from SNMPv2 documents - Add conformance statements',))
if mibBuilder.loadTexts: dpi20MIB.setLastUpdated('9609300000Z')
if mibBuilder.loadTexts: dpi20MIB.setOrganization('IBM Research - T.J. Watson Research Center')
if mibBuilder.loadTexts: dpi20MIB.setContactInfo(' Bert Wijnen Postal: IBM International Operations Watsonweg 2 1423 ND Uithoorn The Netherlands Tel: +31 79-322-8316 E-mail: wijnen@vnet.ibm.com (IBM internal: wijnen at uitvm1)')
if mibBuilder.loadTexts: dpi20MIB.setDescription('The MIB module describing DPI objects.')
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmDPI = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2))
dpiPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 1))
dpiPortForTCP = MibScalar((1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpiPortForTCP.setStatus('current')
if mibBuilder.loadTexts: dpiPortForTCP.setDescription('The TCP port number on which the agent listens for DPI connections. If the value is zero, it means that the agent is not listening for TCP DPI connections.')
dpiPortForUDP = MibScalar((1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpiPortForUDP.setStatus('current')
if mibBuilder.loadTexts: dpiPortForUDP.setDescription('The UDP port number on which the agent listens for DPI packets. If the value is zero, it means that the agent is not listening for UDP DPI packets.')
dpiPathNameForUnixStream = MibScalar((1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpiPathNameForUnixStream.setStatus('current')
if mibBuilder.loadTexts: dpiPathNameForUnixStream.setDescription('The full path name for a connection via an AF_UNIX stream connection. The empty value means the agent has no DPI AF_UNIX support.')
dpiMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 2))
dpiMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1))
dpiMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2))
dpiMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1, 1)).setObjects(("DPI20-MIB", "dpiGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiMIBCompliance = dpiMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dpiMIBCompliance.setDescription('The compliance statement for SNMPv2 entities which implement the dpiMIB (DPI MIB).')
dpiMIBComplianceUnix = ModuleCompliance((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1, 2)).setObjects(("DPI20-MIB", "dpiGroup"), ("DPI20-MIB", "dpiGroupUnix"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiMIBComplianceUnix = dpiMIBComplianceUnix.setStatus('current')
if mibBuilder.loadTexts: dpiMIBComplianceUnix.setDescription('The compliance statement for SNMPv2 entities which implement the dpiMIB (DPI MIB), including the new dpiGroupUnix group.')
dpiGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2, 1)).setObjects(("DPI20-MIB", "dpiPortForTCP"), ("DPI20-MIB", "dpiPortForUDP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiGroup = dpiGroup.setStatus('current')
if mibBuilder.loadTexts: dpiGroup.setDescription('The dpiGroup defines the objects that are used to figure out the DPI ports supported by a DPI 2.0 capable SNMP agent.')
dpiGroupUnix = ObjectGroup((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2, 2)).setObjects(("DPI20-MIB", "dpiPathNameForUnixStream"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiGroupUnix = dpiGroupUnix.setStatus('current')
if mibBuilder.loadTexts: dpiGroupUnix.setDescription('The dpiGroup defines the objects that are used to figure out the DPI ports supported by a DPI 2.0 capable SNMP agent.')
mibBuilder.exportSymbols("DPI20-MIB", dpiPort=dpiPort, dpiMIBComplianceUnix=dpiMIBComplianceUnix, dpiPortForTCP=dpiPortForTCP, dpiPortForUDP=dpiPortForUDP, dpiGroup=dpiGroup, dpiGroupUnix=dpiGroupUnix, ibmDPI=ibmDPI, ibm=ibm, dpiPathNameForUnixStream=dpiPathNameForUnixStream, dpiMIBCompliances=dpiMIBCompliances, dpiMIBGroups=dpiMIBGroups, dpiMIBCompliance=dpiMIBCompliance, dpiMIBConformance=dpiMIBConformance, PYSNMP_MODULE_ID=dpi20MIB, dpi20MIB=dpi20MIB)
