#
# PySNMP MIB module RIVERSTONE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, ModuleIdentity, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Gauge32, Bits, Unsigned32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "ModuleIdentity", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Gauge32", "Bits", "Unsigned32", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 10))
rsTCMIB.setRevisions(('2002-06-17 00:00', '2002-03-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsTCMIB.setRevisionsDescriptions(('Revision #2. RsQueuePolicy, RsDiscardPolicy textual conventions added. These are used by RIVERSTONE-QUEUE-MIB.', 'Revision #1. Provide textual conventions used in RIVERSTONE-CONFIG-MIB. (hgr)',))
if mibBuilder.loadTexts: rsTCMIB.setLastUpdated('200206170000Z')
if mibBuilder.loadTexts: rsTCMIB.setOrganization('Riverstone Networks, Inc.')
if mibBuilder.loadTexts: rsTCMIB.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara, CA 95054 (408) 878-6500 nms-eng@riverstonenet.com http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsTCMIB.setDescription('This mib module defines the textual conventions used in various other Riverstone MIBs.')
class RSConfigErrorCode(TextualConvention, Integer32):
    description = 'A unique value, greater than zero defining the config file transfer operation completion status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidConfig", 5), ("commandCompleted", 6), ("internalError", 7), ("tftpServerError", 8))

class RSFileTransferProtocol(TextualConvention, Integer32):
    description = 'A unique value, greater than zero defining the protocol used for file transfer operation on config files. This list may be modified for later additions.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("tftp", 2), ("rsh", 3), ("scp", 4))

class RSTransferStatus(TextualConvention, Integer32):
    description = 'A unique value, greater than zero defining the status of the previous transfer operation, if any.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("error", 5))

class RSChangeSessionType(TextualConvention, Integer32):
    description = 'A unique value, representing the session type of the change session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("console", 2), ("telnet", 3), ("ssh", 4), ("snmp", 5))

class RsQueuePolicy(TextualConvention, Integer32):
    description = 'The queuing policy for each port is by default priority queuing. In priority queuing, each flow is assigned a priority. The higher priority flows go first. Within the priority queue, the flows are serviced in a first in first out order. If the higher priority queue is never empty, the other queues would starve. In fair queuing, each priority queue is serviced in a round-robin fashion. Weighted fair queuing is fair queing for which each queue is weighted. On the RS platform, priorityQueuing is known as strict priority (SP).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("priorityQueuing", 1), ("fairQueuing", 2), ("weightedFairQueuing", 3))

class RsDiscardPolicy(TextualConvention, Integer32):
    description = 'The policy used by a queue to determine how frames should be dropped.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("lastInFirstOut", 1), ("randomEarlyDetection", 2), ("weightedRandomEarlyDetection", 3))

mibBuilder.exportSymbols("RIVERSTONE-TC-MIB", PYSNMP_MODULE_ID=rsTCMIB, RSFileTransferProtocol=RSFileTransferProtocol, RSChangeSessionType=RSChangeSessionType, rsTCMIB=rsTCMIB, RSConfigErrorCode=RSConfigErrorCode, RsDiscardPolicy=RsDiscardPolicy, RsQueuePolicy=RsQueuePolicy, RSTransferStatus=RSTransferStatus)
