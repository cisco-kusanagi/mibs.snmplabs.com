#
# PySNMP MIB module DEVETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVETHERNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Unsigned32, MibIdentifier, ModuleIdentity, Counter64, IpAddress, Bits, Counter32, iso, ObjectIdentity, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter64", "IpAddress", "Bits", "Counter32", "iso", "ObjectIdentity", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniDevEthernet = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 11))
if mibBuilder.loadTexts: aniDevEthernet.setLastUpdated('0210251725Z')
if mibBuilder.loadTexts: aniDevEthernet.setOrganization('Aperto Networks')
aniDevEthernetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1))
aniDevEthernetConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("auto-negotiate", 1), ("speed-100mbps-full", 2), ("speed-100mbps-half", 3), ("speed-10mbps-full", 4), ("speed-10mbps-half", 5))).clone('auto-negotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEthernetConfigMode.setStatus('current')
aniDevEthernetCurrentLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevEthernetCurrentLinkStatus.setStatus('current')
aniDevEthernetCurrentSpeed = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("speed-10-mbps", 1), ("speed-100-mbps", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevEthernetCurrentSpeed.setStatus('current')
aniDevEthernetCurrentDuplex = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half-duplex", 1), ("full-duplex", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevEthernetCurrentDuplex.setStatus('current')
mibBuilder.exportSymbols("DEVETHERNET-MIB", aniDevEthernetConfigMode=aniDevEthernetConfigMode, aniDevEthernetConfig=aniDevEthernetConfig, aniDevEthernet=aniDevEthernet, PYSNMP_MODULE_ID=aniDevEthernet, aniDevEthernetCurrentDuplex=aniDevEthernetCurrentDuplex, aniDevEthernetCurrentSpeed=aniDevEthernetCurrentSpeed, aniDevEthernetCurrentLinkStatus=aniDevEthernetCurrentLinkStatus)
