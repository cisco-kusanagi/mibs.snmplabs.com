#
# PySNMP MIB module NAGIOS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NAGIOS-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:16:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, NotificationType, TimeTicks, Counter32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, IpAddress, MibIdentifier, enterprises, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "NotificationType", "TimeTicks", "Counter32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "IpAddress", "MibIdentifier", "enterprises", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nagios = ModuleIdentity((1, 3, 6, 1, 4, 1, 20006))
nagios.setRevisions(('2005-03-09 00:00', '2005-01-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nagios.setRevisionsDescriptions(('Spell check', 'Initial Version',))
if mibBuilder.loadTexts: nagios.setLastUpdated('200503090000Z')
if mibBuilder.loadTexts: nagios.setOrganization('Nagios')
if mibBuilder.loadTexts: nagios.setContactInfo(' Subhendu Ghosh Telephone: +1 201 232 2851 Email: sghosh@users.sourceforge.net Nagios Information: http://www.nagios.org ')
if mibBuilder.loadTexts: nagios.setDescription('Objects for Nagios(tm) NMS')
class NotifyType(TextualConvention, Integer32):
    description = 'A string identifying the type of notification that is being sent (PROBLEM, RECOVERY, ACKNOWLEDGEMENT, FLAPPINGSTART or FLAPPINGSTOP). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("problem", 0), ("recovery", 1), ("acknowledgement", 2), ("flappingstart", 3), ("flappingstop", 4))

class HostStateID(TextualConvention, Integer32):
    description = 'A number that corresponds to the current state of the host: 0=UP, 1=DOWN, 2=UNREACHABLE.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3))
    namedValues = NamedValues(("up", 0), ("down", 1), ("unreachable", 3))

class HostStateType(TextualConvention, Integer32):
    description = 'A string indicating the state type for the current host check (HARD or SOFT). Soft states occur when host checks return a non-OK (non-UP) state and are in the process of being retried. Hard states result when host checks have been checked a specified maximum number of times.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("hard", 0), ("soft", 1))

class ServiceStateID(TextualConvention, Integer32):
    description = 'A number that corresponds to the current state of the service: 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("warning", 1), ("critical", 2), ("unknown", 3))

mibBuilder.exportSymbols("NAGIOS-ROOT-MIB", HostStateID=HostStateID, HostStateType=HostStateType, PYSNMP_MODULE_ID=nagios, nagios=nagios, ServiceStateID=ServiceStateID, NotifyType=NotifyType)
