#
# PySNMP MIB module RADLAN-UUSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-UUSC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:41:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, MibIdentifier, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, Bits, Integer32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibIdentifier", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "Bits", "Integer32", "ModuleIdentity", "IpAddress")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
rlUnknowUnicastStormCtrlFastEthernet = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 125))
rlUnknowUnicastStormCtrlFastEthernet.setRevisions(('2007-07-04 00:00',))
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernet.setLastUpdated('200707040000Z')
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernet.setOrganization('Radlan Computer Communications Ltd.')
rlUnknowUnicastStormCtrlFastEthernetRate = MibScalar((1, 3, 6, 1, 4, 1, 89, 125, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernetRate.setStatus('mandatory')
rlUnknowUnicastStormCtrlFastEthernetStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 125, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUnknowUnicastStormCtrlFastEthernetStatus.setStatus('mandatory')
mibBuilder.exportSymbols("RADLAN-UUSC-MIB", rlUnknowUnicastStormCtrlFastEthernetRate=rlUnknowUnicastStormCtrlFastEthernetRate, rlUnknowUnicastStormCtrlFastEthernetStatus=rlUnknowUnicastStormCtrlFastEthernetStatus, PYSNMP_MODULE_ID=rlUnknowUnicastStormCtrlFastEthernet, rlUnknowUnicastStormCtrlFastEthernet=rlUnknowUnicastStormCtrlFastEthernet)
