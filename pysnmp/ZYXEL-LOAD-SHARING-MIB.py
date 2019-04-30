#
# PySNMP MIB module ZYXEL-LOAD-SHARING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-LOAD-SHARING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, ObjectIdentity, TimeTicks, Bits, Counter32, iso, IpAddress, ModuleIdentity, MibIdentifier, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ObjectIdentity", "TimeTicks", "Bits", "Counter32", "iso", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLoadSharing = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44))
if mibBuilder.loadTexts: zyxelLoadSharing.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLoadSharing.setOrganization('Enterprise Solution ZyXEL')
zyxelLoadSharingSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1))
zyLoadSharingState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingState.setStatus('current')
zyLoadSharingCriteria = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("srcIp", 1), ("srcDstIp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingCriteria.setStatus('current')
zyLoadSharingAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingAgingTime.setStatus('current')
zyLoadSharingDiscoverTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingDiscoverTime.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-LOAD-SHARING-MIB", zyLoadSharingAgingTime=zyLoadSharingAgingTime, zyxelLoadSharing=zyxelLoadSharing, zyLoadSharingDiscoverTime=zyLoadSharingDiscoverTime, zyLoadSharingState=zyLoadSharingState, zyxelLoadSharingSetup=zyxelLoadSharingSetup, PYSNMP_MODULE_ID=zyxelLoadSharing, zyLoadSharingCriteria=zyLoadSharingCriteria)
