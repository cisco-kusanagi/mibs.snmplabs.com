#
# PySNMP MIB module ZYXEL-OUT-OF-BAND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-OUT-OF-BAND-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, Unsigned32, iso, ObjectIdentity, IpAddress, TimeTicks, Gauge32, Integer32, Bits, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "ObjectIdentity", "IpAddress", "TimeTicks", "Gauge32", "Integer32", "Bits", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelOutOfBand = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58))
if mibBuilder.loadTexts: zyxelOutOfBand.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelOutOfBand.setOrganization('Enterprise Solution ZyXEL')
zyxelOutOfBandIpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1))
zyOutOfBandIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandIpAddress.setStatus('current')
zyOutOfBandSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandSubnetMask.setStatus('current')
zyOutOfBandGateway = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandGateway.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-OUT-OF-BAND-MIB", zyOutOfBandGateway=zyOutOfBandGateway, zyOutOfBandSubnetMask=zyOutOfBandSubnetMask, zyxelOutOfBand=zyxelOutOfBand, zyOutOfBandIpAddress=zyOutOfBandIpAddress, PYSNMP_MODULE_ID=zyxelOutOfBand, zyxelOutOfBandIpSetup=zyxelOutOfBandIpSetup)
