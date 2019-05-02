#
# PySNMP MIB module CPQRECOV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQRECOV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
cpqHoTrapFlags, compaq = mibBuilder.importSymbols("CPQHOST-MIB", "cpqHoTrapFlags", "compaq")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, ModuleIdentity, iso, Counter64, Gauge32, IpAddress, Unsigned32, Bits, enterprises, NotificationType, ObjectIdentity, Counter32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "iso", "Counter64", "Gauge32", "IpAddress", "Unsigned32", "Bits", "enterprises", "NotificationType", "ObjectIdentity", "Counter32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpqRecovery = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 13))
cpqRsPartnerFailed = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13001)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
if mibBuilder.loadTexts: cpqRsPartnerFailed.setDescription("Recovery Server partner server failure. The Recovery Agent reports that the partner server has failed. This server has taken over the partner's operations.")
cpqRsStandbyCableFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13002)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
if mibBuilder.loadTexts: cpqRsStandbyCableFailure.setDescription('Recovery Server serial interconnect failure. The Standby Recovery Agent reports that the local serial interconnect is not connected or has failed. The primary server is being shutdown in anticipation of the startup of the standby server.')
cpqRsStandbyFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13003)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
if mibBuilder.loadTexts: cpqRsStandbyFailure.setDescription("Recovery Server standby server failure. The Recovery Agent reports that the standby server has failed or the standby's serial interconnect is not connected.")
cpqRsOnlineCableFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13004)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
if mibBuilder.loadTexts: cpqRsOnlineCableFailure.setDescription('On-Line Recovery Server serial interconnect failure. The On-Line Recovery Agent reports that the local serial interconnect is not connected or has failed. However, network operations confirm that the partner is still operating correctly.')
cpqRsFailoverFailed = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13005)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
if mibBuilder.loadTexts: cpqRsFailoverFailed.setDescription('On-Line Recovery Server Failover failure. The On-Line Recovery Agent reports that an attempt to take on the operations of the partner server was attempted and failed.')
mibBuilder.exportSymbols("CPQRECOV-MIB", cpqRsOnlineCableFailure=cpqRsOnlineCableFailure, cpqRecovery=cpqRecovery, cpqRsPartnerFailed=cpqRsPartnerFailed, cpqRsStandbyFailure=cpqRsStandbyFailure, cpqRsStandbyCableFailure=cpqRsStandbyCableFailure, cpqRsFailoverFailed=cpqRsFailoverFailed)
