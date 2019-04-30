#
# PySNMP MIB module EMCGATEWAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EMCGATEWAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
connUnitEventObject, connUnitEventType, connUnitType, connUnitStatus, connUnitEventId, connUnitEventDescr, connUnitEventSeverity, connUnitName, connUnitId, connUnitState = mibBuilder.importSymbols("FCMGMT-MIB", "connUnitEventObject", "connUnitEventType", "connUnitType", "connUnitStatus", "connUnitEventId", "connUnitEventDescr", "connUnitEventSeverity", "connUnitName", "connUnitId", "connUnitState")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, IpAddress, Gauge32, iso, NotificationType, MibIdentifier, ObjectIdentity, Counter64, Integer32, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter64", "Integer32", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

emc = MibIdentifier((1, 3, 6, 1, 4, 1, 1139))
eccGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 1139, 3))
eccGatewayRevision = MibScalar((1, 3, 6, 1, 4, 1, 1139, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eccGatewayRevision.setStatus('mandatory')
eccUnitStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1139, 3) + (0,1)).setObjects(("FCMGMT-MIB", "connUnitStatus"), ("FCMGMT-MIB", "connUnitState"), ("FCMGMT-MIB", "connUnitName"), ("FCMGMT-MIB", "connUnitType"))
eccUnitDeletedTrap = NotificationType((1, 3, 6, 1, 4, 1, 1139, 3) + (0,3)).setObjects(("FCMGMT-MIB", "connUnitId"), ("FCMGMT-MIB", "connUnitName"))
eccUnitEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 1139, 3) + (0,4)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventObject"), ("FCMGMT-MIB", "connUnitEventDescr"), ("FCMGMT-MIB", "connUnitEventSeverity"), ("FCMGMT-MIB", "connUnitName"), ("FCMGMT-MIB", "connUnitType"))
mibBuilder.exportSymbols("EMCGATEWAY-MIB", eccUnitDeletedTrap=eccUnitDeletedTrap, eccGatewayRevision=eccGatewayRevision, emc=emc, eccUnitStatusChange=eccUnitStatusChange, eccUnitEventTrap=eccUnitEventTrap, eccGateway=eccGateway, DisplayString=DisplayString)
