#
# PySNMP MIB module DPI20-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DPI20-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:39:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter64, enterprises, NotificationType, ObjectIdentity, ModuleIdentity, iso, Counter32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter64", "enterprises", "NotificationType", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dpi20MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2, 2, 1))
dpi20MIB.setRevisions(('1996-09-30 00:00', '1996-05-01 00:00', '1995-05-26 00:00',))
if mibBuilder.loadTexts: dpi20MIB.setLastUpdated('9609300000Z')
if mibBuilder.loadTexts: dpi20MIB.setOrganization('IBM Research - T.J. Watson Research Center')
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmDPI = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2))
dpiPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 1))
dpiPortForTCP = MibScalar((1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpiPortForTCP.setStatus('current')
dpiPortForUDP = MibScalar((1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpiPortForUDP.setStatus('current')
dpiPathNameForUnixStream = MibScalar((1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpiPathNameForUnixStream.setStatus('current')
dpiMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 2))
dpiMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1))
dpiMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2))
dpiMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1, 1)).setObjects(("DPI20-MIB", "dpiGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiMIBCompliance = dpiMIBCompliance.setStatus('current')
dpiMIBComplianceUnix = ModuleCompliance((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1, 2)).setObjects(("DPI20-MIB", "dpiGroup"), ("DPI20-MIB", "dpiGroupUnix"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiMIBComplianceUnix = dpiMIBComplianceUnix.setStatus('current')
dpiGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2, 1)).setObjects(("DPI20-MIB", "dpiPortForTCP"), ("DPI20-MIB", "dpiPortForUDP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiGroup = dpiGroup.setStatus('current')
dpiGroupUnix = ObjectGroup((1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2, 2)).setObjects(("DPI20-MIB", "dpiPathNameForUnixStream"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpiGroupUnix = dpiGroupUnix.setStatus('current')
mibBuilder.exportSymbols("DPI20-MIB", PYSNMP_MODULE_ID=dpi20MIB, dpiMIBComplianceUnix=dpiMIBComplianceUnix, dpiMIBCompliance=dpiMIBCompliance, dpiPathNameForUnixStream=dpiPathNameForUnixStream, ibmDPI=ibmDPI, dpiMIBConformance=dpiMIBConformance, dpiGroupUnix=dpiGroupUnix, dpiGroup=dpiGroup, dpiMIBGroups=dpiMIBGroups, dpiPort=dpiPort, ibm=ibm, dpi20MIB=dpi20MIB, dpiMIBCompliances=dpiMIBCompliances, dpiPortForTCP=dpiPortForTCP, dpiPortForUDP=dpiPortForUDP)
