#
# PySNMP MIB module RADLAN-UUSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-UUSC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:50:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, TimeTicks, Counter32, ModuleIdentity, Gauge32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, MibIdentifier, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter32", "ModuleIdentity", "Gauge32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "MibIdentifier", "Counter64", "Bits")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
rlUnknowUnicastStormCtrlFastEthernet = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 125))
rlUnknowUnicastStormCtrlFastEthernet.setRevisions(('2007-07-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernet.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernet.setLastUpdated('200707040000Z')
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernet.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernet.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernet.setDescription('The private MIB module definition for unknown unicast storm control on Diamond Opal.')
rlUnknowUnicastStormCtrlFastEthernetRate = MibScalar((1, 3, 6, 1, 4, 1, 89, 125, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernetRate.setStatus('mandatory')
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernetRate.setDescription('The rate configured for Unknown unicast storm control')
rlUnknowUnicastStormCtrlFastEthernetStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 125, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernetStatus.setStatus('mandatory')
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernetStatus.setDescription('Enable/Disable unknown unicast storm control')
mibBuilder.exportSymbols("RADLAN-UUSC-MIB", rlUnknowUnicastStormCtrlFastEthernet=rlUnknowUnicastStormCtrlFastEthernet, PYSNMP_MODULE_ID=rlUnknowUnicastStormCtrlFastEthernet, rlUnknowUnicastStormCtrlFastEthernetStatus=rlUnknowUnicastStormCtrlFastEthernetStatus, rlUnknowUnicastStormCtrlFastEthernetRate=rlUnknowUnicastStormCtrlFastEthernetRate)
