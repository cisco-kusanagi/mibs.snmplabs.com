#
# PySNMP MIB module CPQRECOV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQRECOV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:12:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
cpqHoTrapFlags, compaq = mibBuilder.importSymbols("CPQHOST-MIB", "cpqHoTrapFlags", "compaq")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Counter32, Gauge32, MibIdentifier, ModuleIdentity, TimeTicks, ObjectIdentity, iso, NotificationType, Counter64, enterprises, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "iso", "NotificationType", "Counter64", "enterprises", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpqRecovery = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 13))
cpqRsPartnerFailed = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13001)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsStandbyCableFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13002)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsStandbyFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13003)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsOnlineCableFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13004)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsFailoverFailed = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13005)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
mibBuilder.exportSymbols("CPQRECOV-MIB", cpqRsStandbyCableFailure=cpqRsStandbyCableFailure, cpqRsStandbyFailure=cpqRsStandbyFailure, cpqRsFailoverFailed=cpqRsFailoverFailed, cpqRecovery=cpqRecovery, cpqRsPartnerFailed=cpqRsPartnerFailed, cpqRsOnlineCableFailure=cpqRsOnlineCableFailure)
