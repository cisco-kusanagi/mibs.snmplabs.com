#
# PySNMP MIB module RIVERSTONE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, Bits, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, TimeTicks, MibIdentifier, iso, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "Bits", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 10))
rsTCMIB.setRevisions(('2002-06-17 00:00', '2002-03-25 00:00',))
if mibBuilder.loadTexts: rsTCMIB.setLastUpdated('200206170000Z')
if mibBuilder.loadTexts: rsTCMIB.setOrganization('Riverstone Networks, Inc.')
class RSConfigErrorCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidConfig", 5), ("commandCompleted", 6), ("internalError", 7), ("tftpServerError", 8))

class RSFileTransferProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("tftp", 2), ("rsh", 3), ("scp", 4))

class RSTransferStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("error", 5))

class RSChangeSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("console", 2), ("telnet", 3), ("ssh", 4), ("snmp", 5))

class RsQueuePolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("priorityQueuing", 1), ("fairQueuing", 2), ("weightedFairQueuing", 3))

class RsDiscardPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("lastInFirstOut", 1), ("randomEarlyDetection", 2), ("weightedRandomEarlyDetection", 3))

mibBuilder.exportSymbols("RIVERSTONE-TC-MIB", RSFileTransferProtocol=RSFileTransferProtocol, rsTCMIB=rsTCMIB, RSConfigErrorCode=RSConfigErrorCode, RsQueuePolicy=RsQueuePolicy, PYSNMP_MODULE_ID=rsTCMIB, RSChangeSessionType=RSChangeSessionType, RsDiscardPolicy=RsDiscardPolicy, RSTransferStatus=RSTransferStatus)
