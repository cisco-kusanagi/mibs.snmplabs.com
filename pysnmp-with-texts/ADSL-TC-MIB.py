#
# PySNMP MIB module ADSL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADSL-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
transmission, IpAddress, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks, Counter32, ModuleIdentity, Unsigned32, NotificationType, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adslMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94))
adsltcmib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 2))
adsltcmib.setRevisions(('1999-08-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adsltcmib.setRevisionsDescriptions(('Initial Version, published as RFC 2662',))
if mibBuilder.loadTexts: adsltcmib.setLastUpdated('9908190000Z')
if mibBuilder.loadTexts: adsltcmib.setOrganization('IETF ADSL MIB Working Group')
if mibBuilder.loadTexts: adsltcmib.setContactInfo(' Gregory Bathrick AG Communication Systems A Subsidiary of Lucent Technologies 2500 W Utopia Rd. Phoenix, AZ 85027 USA Tel: +1 602-582-7679 Fax: +1 602-582-7697 E-mail: bathricg@agcs.com Faye Ly Copper Mountain Networks Norcal Office 2470 Embarcadero Way Palo Alto, CA 94303 Tel: +1 650-858-8500 Fax: +1 650-858-8085 E-Mail: faye@coppermountain.com IETF ADSL MIB Working Group (adsl@xlist.agcs.com) ')
if mibBuilder.loadTexts: adsltcmib.setDescription('The MIB module which provides a ADSL Line Coding Textual Convention to be used by ADSL Lines.')
class AdslLineCodingType(TextualConvention, Integer32):
    description = 'This data type is used as the syntax for the ADSL Line Code.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("dmt", 2), ("cap", 3), ("qam", 4))

class AdslPerfCurrDayCount(TextualConvention, Gauge32):
    description = 'A counter associated with interface performance measurements in a current 1-day (24 hour) measurement interval. The value of this counter starts at zero at the beginning of an interval and is increased when associated events occur, until the end of the 1-day interval. At that time the value of the counter is stored in the previous 1-day history interval, if available, and the current interval counter is restarted at zero. In the case where the agent has no valid data available for this interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchName error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation).'
    status = 'current'

class AdslPerfPrevDayCount(TextualConvention, Gauge32):
    description = 'A counter associated with interface performance measurements during the most previous 1-day (24 hour) measurement interval. The value of this counter is equal to the value of the current day counter at the end of its most recent interval. In the case where the agent has no valid data available for this interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchName error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation).'
    status = 'current'

class AdslPerfTimeElapsed(TextualConvention, Gauge32):
    description = "The number of seconds that have elapsed since the beginning of the current measurement period. If, for some reason, such as an adjustment in the system's time-of-day clock, the current interval exceeds the maximum value, the agent will return the maximum value."
    status = 'current'

mibBuilder.exportSymbols("ADSL-TC-MIB", adsltcmib=adsltcmib, AdslLineCodingType=AdslLineCodingType, AdslPerfPrevDayCount=AdslPerfPrevDayCount, AdslPerfCurrDayCount=AdslPerfCurrDayCount, adslMIB=adslMIB, AdslPerfTimeElapsed=AdslPerfTimeElapsed, PYSNMP_MODULE_ID=adsltcmib)
